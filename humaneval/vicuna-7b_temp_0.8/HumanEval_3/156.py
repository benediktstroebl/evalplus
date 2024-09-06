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
    last_deposit_index = operations.index(last_deposit)
    account_balance = 0
    for index in reversed(range(len(operations)-1)):
        deposit = operations[index]
        deposit_index = operations.index(deposit)
        account_balance += deposit - operations[deposit_index-1]
    account_balance += last_deposit - last_deposit_index
    return account_balance < 0

