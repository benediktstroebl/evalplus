```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < threshold:
                return True
    return False
```

This script defines a function called `has_close_elements` that takes in two parameters: `numbers` which is a list of float and `threshold` which is a float. It then iterates over thea list and compares the current number with every other number, and if it finds any two numbers that are closer than a given threshold, it returns True.