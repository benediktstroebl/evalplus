```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # Sort the list of numbers
    numbers.sort()
   
   
    # Check each element in the sorted list
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if abs(numbers[i]-numbers[j]) < threshold:
            return True
    return False

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 0.0]
return has_close_elements(numbers, 0.8)
```