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
    # This is the same as the previous solution, but it uses a list of pairs, which is a more natural representation for this problem
    # We can then use the second element of each pair to check if the balance is below zero
    for i, (deposit, withdrawal) in enumerate(operations):
        if deposit < 0:
            return True
        if withdrawal < 0:
            return True
    return False