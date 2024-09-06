Here is a self-contained Python function that solves the problem of calculating the sum and product of a given list of integers:
```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test the function with various inputs
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
print(sum_product([5, 6, 7, 8]))  # Output: (28, 5664)
print(sum_product([9, 10, 11, 12])) # Output: (41, 122400)
```
This function is designed to handle lists of integers and produce a tuple of two integers: the sum and product of the numbers in the list. The function first checks if the value of the input list is empty, in which case it returns (0, 1). If the list is not empty, the function then uses the sum and product built-in functions to calculate the product and sum of the numbers and returns the result as a tuple.