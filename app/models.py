from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.TextField()
    email = models.TextField()
    phone = models.TextField()
    is_favorite = models.BooleanField()

def create_contact(name, email, phone, favorite):
    contacts = Contact(name=name, email=email,phone=phone, is_favorite=favorite)
    contacts.save()
    return contacts

def all_contacts():
    return Contact.objects.all()

def find_contact_by_name(name):
    try:
        return Contact.objects.get(name=name)
    except:
        return None

def favorite_contacts():
    return Contact.objects.filter(is_favorite=True)

def update_contact_email(name, new_email):
    contact = Contact.objects.get(name=name)
    contact.email = new_email
    contact.save()

def delete_contact(name):
    contact = Contact.objects.get(name=name)
    contact.delete()

