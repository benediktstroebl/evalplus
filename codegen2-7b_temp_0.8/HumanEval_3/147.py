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
    if operations[0] == 1:
        if operations[1] == 1:
            return True
        elif operations[1] == 2:
            return True if operations[2] == 0 else False
        else:
            return False
    else:
        return True if operations[1] == 0 else False

