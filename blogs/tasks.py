from celery import shared_task
from time import sleep

@shared_task
def sleep_well(duration):
    print('Sleeping for {0} seconds'.format(duration))
    sleep(duration)