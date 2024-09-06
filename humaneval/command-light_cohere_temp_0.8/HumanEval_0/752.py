```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < threshold:
                return True
    return False
``` 
This function checks if any two numbers in the list are closer than the threshold. It uses nested loops to iterate through the list and compare each number with the remaining ones. Then, it returns True if any of these comparisons are True.