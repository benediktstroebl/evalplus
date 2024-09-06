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

    def count_decrease(arr: List[int], pos: int) -> int:
        count = 0
        for i in range(pos, len(arr)):
            if arr[i] < arr[pos]:
                count += 1
        return count

    balance = 0
    for i in reversed(operations):
        balance += i
        if balance < 0:
            return True
    return False

