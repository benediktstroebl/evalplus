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
    last_balance = operations[-3]
    for i in range(len(operations) - 2):
        if operations[i] < 0:
            if last_balance < 0:
                return True
            last_balance = last_withdrawal
        elif operations[i] > last_deposit:
            return True
    return False

