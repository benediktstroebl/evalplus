```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in the given list of numbers, are any two numbers closer to each other than the given threshold
    """
    for i in range(len(numbers) - 1):
        if numbers[i] - numbers[i + 1] < threshold:
            return True
    return False

# Example test
numbers = [1.0, 2.0, 3.0, 0.0, 5.0, 2.0]
threshold = 0.1

print(has_close_elements(numbers, 0.1))  # Should return True
```