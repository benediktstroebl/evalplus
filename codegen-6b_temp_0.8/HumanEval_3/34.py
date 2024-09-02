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
    # we make a new account with first element as 0.
    # if the next element is > 0, we add the difference to the element.
    # if the next element is < 0, we subtract the absolute value of the difference from the element.
    # we keep doing this till we get elements whose next element is 0
    # if the balance falls below 0, this is the point where our function returns True.
    # else, function returns False.
    balance = 0
    for operation in operations:
        if operation > 0:
            balance += operation
        elif operation < 0:
            balance -= abs(operation)
    return balance < 0

