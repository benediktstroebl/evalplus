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
    new_list = []
    for idx, val in enumerate(operations):
        if idx == 0:
            new_list.append(val)
        else:
            new_list.append(val + new_list[-1])
    return new_list[-1] < 0

