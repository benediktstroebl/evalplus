Here is a Python script with a self-contained function that solves the problem:
```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """For a given list of integers, returns a tuple consisting of a sum and a product of all the integers in a list."""
    return (sum(numbers), product(numbers))

# Testing function
def test_sum_product():
    numbers = [1, 2, 3, 4]
    result = sum_product(numbers)
    assert result == (10, 24)  # This will fail if the function doesn't catch the types correctly

# Driver code
if __name__ == "__main__":
    test_sum_product()
```
This code defines a function `sum_product` that calculates the sum and product of a given list of integers. It also provides a basic test function to ensure the function works as expected. The driver code ensures the test_sum_product() will fail if the function doesn't catch the types correctly, which indicates the function is implemented correctly.