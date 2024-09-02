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
    # Вариант с zip
    #
    # total = 0
    # for deposit, withdrawal in zip(operations[::2], operations[1::2]):
    #     total += deposit
    #     total -= withdrawal
    #     if total < 0:
    #         return True
    #
    # return False

    # Вариант без zip
    #
    # total = 0
    # for op in operations:
    #     if total < 0:
    #         return True
    #     total += op if op > 0 else -op
    #
    # return False

    # Вариант с and
    #
    # total = 0
    # for op in operations:
    #     if total < 0 and op > 0:
    #         return True
    #     total += op if op > 0 else -op
    #
    # return False

    # Вариант с модулем
    #
    # total = 0
    # for op in operations:
    #     total += op if op > 0 else -op
    #     if total < 0:
    #         return True
    #
    # return False

    # Вариант с арифметическими операциями (модуль)
    #
    # return any(map(lambda op: op > 0 and total < 0, operations))

    # Вариант с арифметическими операциями (без map)
    #
    # for op in operations:
    #     if op > 0 and total < 0:
    #         return True
    #     total += op if op > 0 else -op
    #
    # return False

    # Вариант с арифметическими операциями (без map и for)
    #
    # return any(total < 0 for total in map(lambda op: op > 0 and total + op or total - op, operations))

