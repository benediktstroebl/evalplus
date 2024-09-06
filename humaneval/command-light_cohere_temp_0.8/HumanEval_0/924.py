```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Checks if in the list of numbers, are any two elements closer than the given threshold
    """
    for i in range(len(numbers) - 1):
        if numbers[i] - numbers[i + 1] < threshold:
            return True
    return False

# Test the function
numbers = [1.0, 2.8, 3.0, 4.8, 5.8]
return has_close_elements(numbers, 0.8)  # False
```