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
    import bisect
    balance = 0
    l = len(operations)
    for i in range(l):
        if operations[i] < 0:
            cur_i = bisect.bisect_left(operations, operations[i])
            if cur_i == l or operations[cur_i] > -operations[i]:
                return True
            else:
                balance -= operations[i]
                bisect.insort(operations, -balance)
    return False

