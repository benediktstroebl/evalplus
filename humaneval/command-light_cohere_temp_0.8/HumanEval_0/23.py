Here is a self-contained Python script with a function that solves the problem:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] - numbers[j] <= threshold:
                return True
    return False
```
The function checks each pair of numbers in the list against the threshold, and returns True if any two numbers are closer to each other.