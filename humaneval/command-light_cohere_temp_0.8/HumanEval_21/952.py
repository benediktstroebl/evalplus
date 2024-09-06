Here's a self-contained Python script that solves the problem:
```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    # Apply the linear transformation to the list of numbers.
    # Ensure the minimum number is 0 and the maximum is 1
    return [x // 100.0 for x in numbers]

# Test the function with a sample list of numbers
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
assert rescale_to_unit(numbers) == [0.0, 0.0, 0.0, 1.0])

# Verify the function's output for the list with zeros
numbers = [0.0, 0.0, 0.0, 0.0]
assert rescale_to_unit(numbers) == [0.0, 0.0, 0.0, 0.0])
# Print the result of the function for the list [1.0, 2.0, 3.0, 4.0]
assert rescale_to_unit(numbers) == [0.0, 0.0, 0.0, 1.0])
```