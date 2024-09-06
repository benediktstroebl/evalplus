```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < threshold:
                return True
    return False
```
This Python script defines a function called has_close_elements that takes two arguments: a list of numbers and a threshold value. The function then loops through every element in the list and checks if the absolute difference between the current element and the next element is less than the threshold. It then returns True if any of these conditions are met.