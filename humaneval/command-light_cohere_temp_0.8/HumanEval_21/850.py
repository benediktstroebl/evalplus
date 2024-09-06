```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Ensure the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two numbers")

    # Apply linear transform
    numbers[0] = min(numbers)
    numbers[1] = max(numbers)

    return numbers

# Example usage
input_numbers = [1.0, 2.0, 3.0, 4.0, 0.0, 5]
print(rescale_to_unit(input_numbers)) == [0.0, 0.0, 0.0, 1.0])
```