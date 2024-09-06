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
    if len(operations) == 1:
        return False
    if len(operations) == 2:
        return operations[1] < operations[0]
    if len(operations) == 3:
        return operations[1] < operations[0] and operations[2] < 0
    if len(operations) > 3:
        balance = 0
        for idx, operation in enumerate(operations):
            if idx == 0:
                continue
            balance += operations[idx]
            if idx == 1:
                if balance < 0:
                    return True
            if idx > 1:
                if operations[idx - 1] < operations[idx] and balance < 0:
                    return True
        return False

