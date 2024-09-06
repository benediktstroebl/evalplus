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
    # your code goes here
    # 3 <- 1
    # 2 <- 3
    # 1 <- 2
    # -1 <- 1
    # -2 <- 1
    # -3 <- 2
    # -4 <- 3
    # -5 <- 4

    if operations is None or operations == []:
        return False
    current = 0
    for operation in operations:
        current += operation
        if current < 0:
            return True
    return False
