from django.db import models
from django.utils.translation import gettext_lazy as _


class studentsData(models.Model):

    name = models.CharField(_('Student Name'), max_length=255)
    age = models.IntegerField(_('Age'),)
    gender = models.CharField(_('Gender'), max_length=10)
    address = models.CharField(_('Address'), max_length=255)
    email = models.EmailField(_('Email'), )
    phone = models.IntegerField(_('Phone No.'), )
    courses = models.CharField(_('Courses'), max_length=255)
    gpa = models.DecimalField(_('GPA'), decimal_places= 2, max_digits=4)
    
    class Meta:
        verbose_name = _("studentsData")
        verbose_name_plural = _("studentsData")
        
    def __str__(self): 
        return self.name
