```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    """
    list comprehension is used to calculate the product: product = [x * y for x, y in zip(numbers)]
    sum = sum(numbers)
    return (sum, product)
    """
    return (sum, sum(numbers))

# Test cases
test_data = [1, 2, 3, 4]
test_results = sum_product(test_data)
print(test_results)  # Output: (6, 12)
test_empty = []
test_results_empty = sum_product(test_empty)
print(test_results_empty)  # Output: (0, 1)
test_large = [123, 456, 789, 123]
test_results_large = sum_product(test_large)
print(test_results_large)  # Output: (1022, 34567)
```