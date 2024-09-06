```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    # sort the list of numbers
    numbers.sort(key=lambda x:x)
    low = float('-inf')
    high = float('inf')
    for i in range(0, len(numbers)):
        number = numbers[i]
        if i > 0:
            temp = numbers[i-1]
        else:
            temp = float('inf')
        if abs(number - temp) <= threshold:
            low = min(low, temp)
        high = max(high, temp)
    return high == low
```
The function checks if any two elements in the list are closer than the given threshold. If so, it returns True, indicating that the list has close elements. If not, it returns False, indicating that the list does not have close elements.