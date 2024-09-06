```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # Sorting the list of numbers
    numbers.sort(key=lambda x: x)
    
    # We will check the adjacent elements which are next to each other
    # in the sorted list
    for i in range(1, len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[j] - numbers[i] < threshold:
                return True
    
    return False
```
This function will return true if the given list of numbers has any two elements that are closer to each other than the given threshold.