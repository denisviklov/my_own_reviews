from django.contrib import admin

# Register your models here.
from .models import ProffesionalReview,PersonalReview

admin.site.register(ProffesionalReview)
admin.site.register(PersonalReview)
