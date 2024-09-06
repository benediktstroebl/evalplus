```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculates the sum and product of a list of integers. For empty list, the result is 0 and 1.
    """
    return (sum(numbers), product(numbers))
numbers = [1, 2, 3, 4]
print(sum_product(numbers))  # Output: (10, 24)
print(sum_product([]) )  # Output: (0, 1)
print(sum_product([1, 2, 3, 4, 5])) # Output: error: TypeError: tuple object '[]' does not support item assignment
```