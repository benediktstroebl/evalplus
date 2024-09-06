```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # Check if in list of numbers, any two elements are closer than given threshold
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if math.sqrt((numbers[j]) < threshold:
                return True
    return False
```
This Python function, has_close_elements, takes a list of numbers and a threshold as input. It loops two elements to compare the elements of the list and returns a boolean value that indicates if there are any two numbers in the list that are closer than the threshold.