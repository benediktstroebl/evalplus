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
    for i in range(len(operations) - 1):
        if operations[i] > 0 and operations[i+1] < 0:
            return True
    return False

if __name__ == '__main__':
    operations = List(int)
    operations.append(1)
    operations.append(2)
    operations.append(3)
    operations.append(-4)
    operations.append(5)

    below_zero(operations)