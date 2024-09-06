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
        return False
    res = []
    for i in range(0, len(operations)):
        if operations[i] > 0:
            res.append(operations[i])
        elif operations[i] < 0:
            if res:
                res[-1] = res[-1] + operations[i]
            else:
                res.append(operations[i])
    if res and res[-1] < 0:
        return True
    return False

