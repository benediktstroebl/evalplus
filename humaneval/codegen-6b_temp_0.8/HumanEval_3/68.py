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
    if any(operations):
        balance = 0
        for elem in operations:
            if elem > balance:
                return True
            else:
                balance = balance - elem
        return False
    else:
        return False


assert below_zero([1, 2, 3]) == False
assert below_zero([1, 2, -4, 5]) == True
assert below_zero([]) == False
assert below_zero([-1, -2, -3]) == False