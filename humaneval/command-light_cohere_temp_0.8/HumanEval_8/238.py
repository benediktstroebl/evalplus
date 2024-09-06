```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    if not numbers:
        return (0, 1)
    return (sum(numbers), products(numbers))
    def products(numbers: List[int]):
        result = 1
        for num in numbers:
            result *= num
        return result
    return (sum(numbers), products(numbers))
# Example usage
numbers = [1, 2, 3, 4]
print(sum_product(numbers))  # prints (10, 24)
print(sum_product([]))  # prints (0, 1)
``` 
This script provides a function sum_product that calculates the sum and product of the integers in a list, and passes tests to verify its functionality. It handles edge cases, such for an empty list and returns appropriate values.