```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Ensure length of numbers list is at least 2
    if len(numbers) < 2:
        raise ValueError("List of numbers must contain at least two elements")
    # Apply linear transformation to numbers list
    numbers[0] = min(numbers)
    numbers[1] = max(numbers)
    numbers[2] = (numbers[0] - numbers[1]) / (numbers[1] - numbers[0])
    return numbers[2:]
```