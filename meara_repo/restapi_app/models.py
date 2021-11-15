from django.db import models as m

# Create your models here.

class System(m.Model):
    name = m.CharField(max_length=128)
    created = m.DateTimeField('Date/Time created')

class Organization(m.Model):
    name = m.CharField(max_length=128)
    created = m.DateTimeField('Date/Time created')

class Application(m.Model):
    name = m.CharField(max_length=128)
    created = m.DateTimeField('Date/Time created')
