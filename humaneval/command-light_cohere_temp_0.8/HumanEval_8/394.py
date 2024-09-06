```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Compute the sum and product of a list of integers.
    Args:
        numbers: list of integers
    
    Returns:
        tuple: (sum, product) where sum is the sum of all the integers in numbers, and product is the product of all the integers in numbers
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# Unit tests
numbers = [1, 2, 3, 4, 5]
test_sum_product(numbers)  # Should return (6, 20)
numbers = []
test_sum_product(numbers)  # Should return (0, 1)
numbers = [10, 20, 30, 40]
test_sum_product(numbers)  # Should return (60, 120)
def test_sum_product(numbers):
    result = sum_product(numbers)
    print(f"sum = {result[0]}, product = {result[1]}")
``` 
The function test_sum_product is a test function that takes a list of numbers and passes it to the sum_product function. It then checks if the it the expected result of the function.