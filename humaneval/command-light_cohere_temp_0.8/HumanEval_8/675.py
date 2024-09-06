```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of all the integers in a list.
    Args:
        numbers (List[int]): A list of integers
    Returns:
        Tuple[sum, product]: A tuple containing the sum and product of all the integers in the list
    """
    return (sum(numbers), product(numbers))

# Testing function to test the sum_product function
def test_sum_product():
    numbers = [1, 2, 3, 4]
    result = sum_product(numbers)
    assert result == (10, 24)
```
The provided code defines a function sum_product that calculates the sum and product of a given list of integers. The function uses the mathematical operations to compute the sum and product, and returns a tuple of the result. Additionally, there's a testing function test_sum_product that uses the sum_product function to pass a test case, and checks if the result is correct. The code effectively solves the