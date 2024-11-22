from django.db import models
from django.conf import settings


class Todo(models.Model):
    title= models.CharField(max_length=255)
    description = models.TextField(null=True)
    is_complete = models.BooleanField(null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="todo",
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # return f'{self.user.first_name}-{self.title}'
        return self.title