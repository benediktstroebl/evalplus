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
    balance = 0
    current_balance = balance
    for operation in operations:
        if operation < 0:
            current_balance = balance + operation
            balance = current_balance - current_balance % 5
        elif balance == 0:
            balance = 10**len(operations)
        else:
            balance = balance - 1
    return not balance == current_balance

