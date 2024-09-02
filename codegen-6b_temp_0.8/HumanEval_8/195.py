from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    numbers_length = len(numbers)
    if numbers_length < 2:
        return 0, 1

    left_sum = 0
    left_product = 1
    for index in range(numbers_length):
        current_left_sum = numbers[index] + left_sum
        current_left_product = numbers[index] * left_product
        left_sum = current_left_sum
        left_product = current_left_product

    right_sum = 0
    right_product = 1
    for index in range(numbers_length - 1, -1, -1):
        current_right_sum = numbers[index] + right_sum
        current_right_product = numbers[index] * right_product
        right_sum = current_right_sum
        right_product = current_right_product

    return left_sum, left_product * right_product

