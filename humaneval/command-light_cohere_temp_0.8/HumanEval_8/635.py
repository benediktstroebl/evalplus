```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ 
    Returns a tuple consisting of a sum and a product of all the integers in a list.
    """
    sum = 0
    product = 1
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Test the function with different inputs
numbers = [1, 2, 3, 4, 5]
result = sum_product(numbers)
print(f"Sum: {result[0]}, Product: {result[1]}")  # Output: (15, 120)

numbers = []
result = sum_product(numbers)
print(f"Sum: {result[0]}, Product: {result[1]}")  # Output: (0, 1)

numbers = [1, 2, 3, 4, 5, 6]
result = sum_product(numbers)
print(f"Sum: {result[0]}, Product: {result[1]}")  # Output: (20, 720)
```

This Python code defines a function called sum_product, which takes a list of integers as input and returns a tuple with the sum and product of the integers. The function then performs the calculation using a loop and returns the result.

It is then tested with different inputs, and the results are printed to the console.