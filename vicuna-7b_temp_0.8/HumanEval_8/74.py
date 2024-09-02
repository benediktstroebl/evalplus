from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    # Empty list should return 0 and 1
    if not numbers:
        return 0, 1

    # If the list has only one number, we add 1 to the number and return the sum and product
    if len(numbers) == 1:
        number = numbers[0]
        return number + 1, number * number

    # If the list has two numbers, calculate the sum and product of the numbers
    sum, product = 0, 1
    for i in range(len(numbers)):
        sum += numbers[i]
        product *= numbers[i]

    return sum, product
