Here's the solution:
```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:  # handle empty list
        return (0, 1)
    return (sum(numbers), product(numbers))

# test cases
sum_product([]) == (0, 1)
sum_product([1, 2, 3, 4]) == (10, 24)
```
The function handles the edge case of an empty list and then uses the sum and product built-functions to calculate the sum and product of the numbers, respectively.

The test cases also cover the function's expected behavior.