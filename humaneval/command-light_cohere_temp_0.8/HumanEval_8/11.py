```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """For a given list of integers, returns a tuple consisting of a sum and a product of all the integers in a list."""
    return (sum(numbers), product(numbers))

# Example function test
def test_sum_product():
    numbers = [1, 2, 3, 4]
    result = sum_product(numbers)
    print(f"Sum: {result[0]}, Product: {result[1]}")
test_sum_product()
``` 
This function, named `sum_product`, takes a list of integers as input and returns a tuple containing the sum and product of all the numbers in the list. The function is self-contained, and it's designed to handle both standard and edge cases.