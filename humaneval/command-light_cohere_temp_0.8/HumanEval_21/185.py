```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply the linear transform
    numbers_rescale = [num / min(numbers) for num in numbers]
    return numbers_rescale

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 0.0]
numbers_rescale = rescale_to_unit(numbers)

# Test 1: Check if the list is of length greater than 1
result = rescale_to_unit([1.0, 2.0, 3.0, 4.0, 0.0])
assert len(result) > 1

# Test 2: Check if the result is correct after printing
print("Result:", result)

# Test 3: Check if the smallest value in the result is equal to 0
assert min(result) == 0

# Test 4: Check if the largest value in the result is equal to 1
assert max(result) == 1

This script defines a function `rescale_to_unit` that scales a list of numbers to a range where the smallest number is 0 and the largest is 1. The function uses the list's elements to find the smallest value and divides each by that value to scale it to 0 to 1. The result list is then returned.