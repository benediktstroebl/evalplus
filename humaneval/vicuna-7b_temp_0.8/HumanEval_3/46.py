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
    last_deposit = 0
    for operation in operations:
        if operation == -1:
            # If we have a withdrawal, and the last deposit was negative, that means the balance has fallen below zero
            if last_deposit >= 0:
                return True
            last_deposit += 1
        elif operation > 0:
            # If we have a deposit, and the last deposit was positive, that means the balance has risen above zero
            if last_deposit < 0:
                return True
            last_deposit = operation
    return False