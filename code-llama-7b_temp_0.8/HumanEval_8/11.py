from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    # empty sum
    if len(numbers) == 0:
        return 0, 1

    # empty product
    elif len(numbers) == 1:
        return numbers[0], 1

    # sum and product of first two integers in a list
    elif len(numbers) == 2:
        return sum(numbers), numbers[0] * numbers[1]

    # for a longer list, sum and product are calculated recursively
    else:
        # sum of first and last elements of the list and product of first and last elements of the list
        sum_first_and_last = sum([numbers[0], numbers[-1]])
        product_first_and_last = numbers[0] * numbers[-1]

        # recursive calls
        sum_reminder, product_reminder = sum_product(numbers[1:-1])

        # final sum and product
        return (sum_first_and_last + sum_reminder), (product_first_and_last * product_reminder)

