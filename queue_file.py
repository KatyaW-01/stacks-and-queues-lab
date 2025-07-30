import random

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        # TODO: Remove and return the item from the front of the queue
        pass

    def peek(self):
        # TODO: Return the item at the front of the queue without removing it
        pass

    def is_empty(self):
        # TODO: Return True if the queue is empty
        pass

    def select_and_announce_winner(self):
        """
        Randomly selects a winner from the queue.
        Dequeues all items up to and including the winner.
        Returns the name of the winning customer.
        """
        # TODO: Implement winner selection and dequeue process
        pass
