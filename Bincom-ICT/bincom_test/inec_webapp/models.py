from django.db import models

# Create your models here.

class AgentName(models.Model):
	firstName = models.CharField(max_length=255, null=False)
	lastName = models.CharField(max_length=255, null=False)
	email = models.CharField(max_length=255, null=False, default="@example.com")
	phone = models.CharField(max_length=13, null=False)

class AnnouncedLGAResult(models.Model):
	lgaName = models.CharField(max_length=50, null=False)
	partyAbbreviation = models.CharField(max_length=4, null=False)
	partyScore = models.IntegerField(max_length=255, null=False, default="@example.com")
	enteredByUser = models.CharField(max_length=50, null=False)
	dateEntered = models.DateTimeField(null=False)
	userIPAddress = models.CharField(max_length=50, null=False)

class AnnouncedPUResult(models.Model):
	pollinUnitUniqueid = models.CharField(max_length=50, null=False)
	partyAbbreviation = models.CharField(max_length=4, null=False)
	partyScore = models.IntegerField(max_length=255, null=False, default="@example.com")
	enteredByUser = models.CharField(max_length=50, null=False)
	dateEntered = models.DateTimeField(null=False)
	userIPAddress = models.CharField(max_length=50, null=False)

class AnnouncedStateResult(models.Model):
	stateName = models.CharField(max_length=50, null=False)
	partyAbbreviation = models.CharField(max_length=4, null=False)
	partyScore = models.IntegerField(max_length=11, null=False, default="@example.com")
	enteredByUser = models.CharField(max_length=50, null=False)
	dateEntered = models.DateTimeField(null=False)
	userIPAddress = models.CharField(max_length=50, null=False)
