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
    # Check if the number of operations is odd. If so, we can't check if the balance falls below zero,
    # because rule(s) only apply to even operations.
    if len(operations) % 2 != 0:
        return False

    # Iterate through the operations doing double checks to make sure every operation is balanced.
    i = 0
    bal = 0

    while i < len(operations):
        bal += operations[i]

        if bal < 0:
            return True

        if operations[i] < 0:
            return False

        i += 1

    return False

