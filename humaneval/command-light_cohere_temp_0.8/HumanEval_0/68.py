Here's a self-contained Python function that checks if any two numbers in a given list are closer than a given threshold:

```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    """
    return any two elements in the numbers list are closer than the threshold, return True
    """
    for i in range(len(numbers)//2):
        for j in range(i+i+1, len(numbers)):
            if numbers[i] - numbers[j] < threshold:
                return True
    return False
```
This function loops over half of the list and compares each number in the list with the next number, and checks if they are closer than the threshold. 

It returns True if any two numbers are closer than the threshold, and False otherwise.