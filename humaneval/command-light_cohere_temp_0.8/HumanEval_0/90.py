```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # implementing the function
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] - numbers[j] <= threshold:
                return True
    return False

# testing the function
numbers = [1.0, 2.0, 3.0, 0.8, 4.0, 5.0, 2.0]

n = has_close_elements(numbers, 0.8)
print(n)
``` 

This script defines a function `has_close_elements` that checks whether any two consecutive elements in the given list are closer than each other than the specified threshold. The function iterates over the list and compares each pair of elements. Then, it returns True if any pair of elements are closer than the threshold.