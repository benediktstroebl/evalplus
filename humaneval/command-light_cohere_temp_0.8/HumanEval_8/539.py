```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple containing sum and product of integers in a list.
    If the list is empty, return (0, 1)
    If list is not empty, sum(numbers) calculates the sum, product(numbers)** calculates the product, and the function returns the result."""
    if not numbers:
        return (0, 1)
    
    return (sum(numbers), product(numbers))

# Unit tests
test_sum_product = [
    "Given empty list, should return (0,1)",
    "Given list with single element [1], should return (1,1)",
    "Given list with two elements [1,2], should return (3,4)",
    "Given list with more than two elements, should return correctly"
]
print(sum_product(test_sum_product))
```