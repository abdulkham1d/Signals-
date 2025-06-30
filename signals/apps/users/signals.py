from django.dispatch import receiver
from django.db.models.signals import post_init, pre_save, post_save, pre_delete, post_delete, pre_migrate, post_migrate, m2m_changed
from apps.users.models import *


@receiver(post_init, sender=User)
def user_post_init(instance, sender, **kwargs):
    print(f'{instance=} {sender=} {kwargs=}')
    instance.first_name = 'New First Name'
    instance.save()


@receiver(pre_save, sender=PhoneNumber)
def phone_number_pre_save(instance, sender, **kwargs):
    print(f'{instance=} {sender=} {kwargs=}')
    instance.phone_number = 'new phone number'
    instance.save()



@receiver(post_save, sender=PhoneNumber)
def phone_number_post_save(instance, sender, created, **kwargs):
    print(f'{instance=} {sender=} {created=} {kwargs=}')


@receiver(pre_delete, sender=User)
def user_pre_delete(instance, sender, **kwargs):
    print(f'{instance=} {sender=} {kwargs=}')


@receiver(post_delete, sender=User)
def user_post_delete(instance, sender, **kwargs):
    print(f'{instance=} {sender=} {kwargs=}')


@receiver(post_migrate)
def post_migrate(sender, **kwargs):
    print(sender, kwargs)



@receiver(m2m_changed, sender=PhoneNumber)
def tags_changed(sender, instance, action, **kwargs):
    print(sender, instance)
    if action == "post_add":
        print(f"Добавлены теги в {instance.title}")
    elif action == "post_remove":
        print(f"Удалены теги из {instance.title}")
    elif action == "post_clear":
        print(f"Все теги удалены из {instance.title}")