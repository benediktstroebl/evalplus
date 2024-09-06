```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Compute the sum and product of a list of integers.
    Args:
    numbers: list of integers
    Returns:
    tuple: (sum, product) where sum is the sum of the numbers in numbers, and product is the product of the numbers in numbers
    """
    if not numbers:
        return (0, 1)
    
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test case
my_numbers = [1, 2, 3, 4]
result = sum_product(my_numbers)
print(result)  # Prints (10, 24)
```
This code provides a self-contained solution to the problem by defining the sum_product function that calculates the sum and product of a list of integers, passing tests using the test case provided. The code is a way to understand how the function works and how it returns the result.