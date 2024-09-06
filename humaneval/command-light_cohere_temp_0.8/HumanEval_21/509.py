Here is a self-contained Python script that solves the problem you described:
```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    # Ensure the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Apply the rescaling transformation
    numbers[0] = min(numbers)
    numbers[0] = max(numbers)
    new_numbers = [numbers[0] / numbers[1] for numbers in numbers[1:]]
    return new_numbers

# Test case
input_numbers = [1.0, 2.0, 3.0, 4.0, 0.0, 0.0]
expected_result = [0.0, 0.0, 0.0, 0.0]

# Print the result
print(expected_result)
```