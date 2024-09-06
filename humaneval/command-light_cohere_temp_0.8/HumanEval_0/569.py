```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    numbers = sorted(numbers)
    for i in range(1, len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] - numbers[j] <= threshold:
                return True
    return False
``` 
This script defines a function `has_close_elements` that checks if any two numbers in a given list are closer than a given threshold. The function uses the sorting function to sort the list of numbers and then loops through the sorted list to compare each pair of numbers. The function returns `True` if any of these comparisons return `True`. 

This function is self-contained and does not require any additional imports or variables from other modules.