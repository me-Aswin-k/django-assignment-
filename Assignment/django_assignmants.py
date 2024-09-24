#QUESTION 1: : By default are django signals executed synchronously or asynchronously? 
#              Please support your answer with a code snippet that conclusively proves your stance. 
#              The code does not need to be elegant and production ready, we just need to understand your logic.
#==>By default,Django signals are executed synchronously, meaning they run in the same thread as the request or the operation that triggers them. 
#              This can impact performance because the signal handler is executed immediately after the signal is sent, 
#              and the request will not complete until the signal handler finishes


from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
import time


class Car(models.Model):

    name=models.CharField(max_length=150)

    @receiver(pre_save,sender=Car)
    def car_pre_save_handler(sender,instance,**kwargs):

        print("Signal handler started")

        time.sleep(3) #pausing for 3 seconds to simulate a time-consuming operation

        print("Signal handler completed")






#Question 2: Do django signals run in the same thread as the caller? 
#            Please support your answer with a code snippet that conclusively proves your stance. 
#            The code does not need to be elegant and production ready, we just need to understand your logic.
#==>	Yes, by default, Django signals run in the same thread as the caller. 
#            This means that the signal handler will block the caller’s execution until it finishes running


from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
import threading

class Car(models.Model):

    name=models.CharField(max_length=150)

    @receiver(post_delete,sender=Car)
    def car_post_delete_handler(sender,instance,**kwargs):

        current_thread=threading.current_thread()

        print(f"Thread ID in Signal handler:{current_thread.ident}")

        print(f"Is Main thread ? {current_thread is threading.main_thread()}")





#Question 3: By default do django signals run in the same database transaction as the caller? 
#            Please support your answer with a code snippet that conclusively proves your stance. 
#            The code does not need to be elegant and production ready, we just need to understand your logic.

#==> Yes,by default Django signals such as post_save run within the same database transaction as the caller. 
#           If the caller rolls back the transaction,the signal handler's operations are also rolled back.


from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyModel(models.Model):

    name = models.CharField(max_length=100)

class Log(models.Model):
    
    message = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):

    # The signal will create a log entry when MyModel is saved
    print("Signal handler: Creating log entry...")

    Log.objects.create(message=f"Created MyModel with id {instance.id}")
