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
    if len(operations) == 0:
        return True
    elif len(operations) == 1:
        return operations[0] > 0
    elif len(operations) == 2:
        return operations[1] > 0 and operations[0] < 0
    else:
        return below_zero(operations[1:]) and operations[0] <
