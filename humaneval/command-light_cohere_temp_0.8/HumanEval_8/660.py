```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculate the sum and product of a list of integers.
    return:
            a tuple with the sum and product of the list

    :param numbers: List[int], list of integers
    :return: Tuple[int, int], tuple with sum and product of the list
    """
    if not numbers:  # empty list
        return (0, 1)
    
    sum_product = sum(numbers) * product(numbers)  # sum and product using built-in functions
    return (sum_product, sum_product * len(numbers))  # return tuple with sum and product
```