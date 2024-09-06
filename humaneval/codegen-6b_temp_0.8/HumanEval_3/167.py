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
    for i in range(len(operations)):
        for j in operations:
            if i == len(operations) - 1:
                return True
            if operations[i] > 0:
                operations[i] += j
            else:
                operations[i] += j
                return False

