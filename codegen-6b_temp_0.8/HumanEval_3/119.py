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
    #Initialize list of changes for easier access
    changes = []
    for i in range(2, len(operations)):
        changes.append(operations[i] - operations[i-1])
    print(changes)
    for i in range(len(changes)):
        if changes[i] < 0:
            return True
    return False

