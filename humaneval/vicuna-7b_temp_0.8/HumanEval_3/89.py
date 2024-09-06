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

    start = 0
    for i in range(len(operations)):
        if operations[i] > 0:
            start = i
            while operations[i] > 0:
                i += 1
        elif operations[i] < 0:
            if start + 1 in [j for j in range(i) if operations[j] > 0]:
                return True
        else:
            return True
    return False

