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
    # 1) Проверяем есть ли отрицательные значения в списке
    # 2) Находим индекс, в котором отрицательное значение, смотрим на предыдущие значения
    balance = 0
    for operation in operations:
        balance += operation
        if operation < 0:
            return True
        elif balance < 0:
            return True
    return False

