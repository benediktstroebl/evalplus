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

    # first, we need to calculate the balance for each of operations
    # balance[i] is the balance after the i-th operation
    balance = []
    for i in range(len(operations)):
        if i == 0:
            balance.append(operations[i])
        else:
            balance.append(balance[i-1] + operations[i])
    # now we can check if the last element of the balance is negative
    if balance[-1] < 0:
        return True
    return False

