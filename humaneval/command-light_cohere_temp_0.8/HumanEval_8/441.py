```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    If the empty sum should be equal to 0 and empty product should be equal to 1.
    return:
        (sum(numbers), product(numbers))
    """
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))
# Example usage:
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(result)  # Output: (10, 24)
``` 
This function uses the sum and product built-in functions to calculate the sum and product of a list of integers, respectively. You can use this also to pass your own lists of integers to solve problems.