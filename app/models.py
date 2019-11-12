from django.db import models

class DonorModel(models.Model):
    d_name = models.CharField(max_length=30)
    d_user_id = models.CharField(max_length=30)
    d_password = models.CharField(max_length=30)
    d_gender = models.CharField(max_length=30)
    d_mail = models.CharField(max_length=30)
    d_contact_no = models.IntegerField(primary_key=True)
    d_last_donated = models.DateField()
    d_blood_group = models.CharField(max_length=30)
    d_weight = models.FloatField()
    d_state = models.CharField(max_length=30)
    d_city = models.CharField(max_length=30)



class OrganizationModel(models.Model):
    org_name = models.CharField(max_length=30)
    org_user_id = models.CharField(max_length=30,primary_key=True)
    org_password = models.CharField(max_length=30)
