```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple with sum and product of all the integers in a list.
    if not numbers:  # Empty list returns (0,1)
        return (0,1)
    a,b = sum_product([1,2,3,4])
    print(f"Sum: {a}, Product: {b}")
    """

# Test the function
numbers = [1,2,3,4]
sum, product = sum_product(numbers)
print(f"Sum: {sum}, Product: {product}")  # Prints (6, 24)
```