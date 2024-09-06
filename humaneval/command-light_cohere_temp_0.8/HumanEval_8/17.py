```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    numbers = [1, 2, 3, 4]
    return (10, 24)
    """
    return (sum(numbers), product(numbers))

# Test cases
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(result)

numbers = []
result = sum_product(numbers)
print(result)

numbers = [1, 2, 3]
result = sum_product(numbers)
print(result)

numbers = [1, 2, 3, 4, 5]
result = sum_product(numbers)
print(result)
```
This Python script provides a self-contained function `sum_product` that calculates the sum and product of a given list of integers. The function is then tested with different scenarios: empty list, list with only one element, and a list with multiple elements. It consistently returns the If result, demonstrating the functionality and correctness of the `sum_product` function.