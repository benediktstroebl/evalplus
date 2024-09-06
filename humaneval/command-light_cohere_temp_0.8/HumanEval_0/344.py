Here's a self-contained Python script that solves the problem:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    numbers = sorted(numbers)
    for i in range(1, len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[i] - numbers[j] <= threshold:
                return True
    return False
```
This function takes a list of numbers and a threshold as input and returns a boolean value indicating whether any two numbers in the list are closer to each other than the threshold. The function uses a sorting of the numbers and a nested loop to check for each pair of numbers in the list.