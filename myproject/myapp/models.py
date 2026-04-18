from django.db import models


class Project(models.Model):
    CATEGORY_CHOICES = [
        ('web-app', 'Web App'),
        ('smart-contract', 'Smart Contract'),
        ('dashboard', 'Dashboard'),
    ]

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('completed', 'Completed'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES
    )

    demo_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)

    # 🔥 TAMBAHAN WAJIB (biar tidak error lagi)
    tech_stack = models.TextField(
        blank=True,
        null=True,
        help_text="Pisahkan dengan koma, contoh: Laravel, React, MySQL"
    )

    # 🔥 BONUS (biar UI kamu keren)
    image = models.ImageField(
        upload_to='projects/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def tech_list(self):
        """Convert string ke list"""
        if self.tech_stack:
            return [tech.strip() for tech in self.tech_stack.split(',')]
        return []

    def __str__(self):
        return self.title