from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    # Check if the list is empty or not
    if not numbers:
        return 0, 1

    # Create a 2D list with 1 less dimension than the original list
    n = len(numbers)
    m = n // 2
    product = [1] * m
    sum = 0
    for i in range(m):
        for j in range(i+1, n):
            sum += numbers[j]
            product[i] *= numbers[j]

    # Multiply product by (n - i + 1) and add sum to get the final product
    for i in range(m):
        product[i] *= (n - i + 1)
        sum += product[i]

    # Return the sum and product
    return sum, product[0] * product[1]

