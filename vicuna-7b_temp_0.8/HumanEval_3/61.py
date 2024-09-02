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
    last_withdrawal = operations[-2]
    if last_deposit > 0:
        balance = operations[-1]
    else:
        balance = last_withdrawal + operations[-2] - 1

    for op in operations:
        if op < 0:
            return True
        balance -= op

    return balance > 0

