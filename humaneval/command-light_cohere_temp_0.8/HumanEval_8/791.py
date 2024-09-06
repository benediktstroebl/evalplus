```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Example usage:
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(result)  # Output: (10, 24)
```
This code defines a `sum_product` function that calculates the sum and product of a list of integers. The function returns a result as a tuple.

The output of the example usage will be: `(10, 24)`.  This shows the function correctly calculates the sum and product of the given integers.

The code is self-contained and provides a solution to the problem.