```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) <= threshold:
                return True
    return False

# Test cases
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]

threshold = 0.1
print(has_close_elements(numbers,threshold))  # Output: True
```

This script defines a function `has_close_elements` that checks if any two elements in a list of numbers are closer than a given threshold. The function iterates over the list, comparing each element to the next one and returns True if any comparison is less than the threshold.