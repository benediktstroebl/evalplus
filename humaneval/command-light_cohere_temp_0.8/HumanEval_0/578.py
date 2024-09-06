```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    numbers = sorted(numbers)
    for i in range(1, len(numbers)):
        if numbers[i-1] - numbers[i] < threshold:
            return True
    return False
```
The function has_close_elements takes a List[float] called numbers and a float threshold as input and returns a boolean value. It uses the sorting function and loops through the numbers in the list and checks if any two consecutive numbers are closer than the given threshold.