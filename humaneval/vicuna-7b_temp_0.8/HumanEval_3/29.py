from typing import List


def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fallls below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    """
    last_deposit = operations[-1]
    balance = 0
    for i, operation in enumerate(operations):
        if operation < 0:
            balance += operation
            last_deposit = operations[i+1] if i+1 < len(operations) else 0
        else:
            balance += operation
    return balance >= 0

