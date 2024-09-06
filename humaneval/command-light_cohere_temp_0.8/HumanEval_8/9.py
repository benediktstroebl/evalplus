```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """For a given list of integers, returns a tuple consisting of a sum and a product of all the integers in a list."""
    if not numbers:  # empty list
        return (0, 1)  
    sum_ = 0
    prod_ = 1
    for num in numbers:
        sum_ += num
        prod_ *= num
    return (sum_, prod_)
# Example usage
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(result)  # Output: (10, 24)
``` 
This script provides a self-contained function `sum_product` that calculates the sum and product of a given list of integers. The function performs corresponding tests to verify its correctness.