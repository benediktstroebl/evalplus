```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.
    >>> Test if the has any two elements in the list that are closer than threshold.
    >>> Test the return True if any elements are closer than the threshold, otherwise False
    """
    for i in range(len(numbers) - 1):
        if numbers[i] < numbers[i+1] <= threshold:
            return True
    return False
``` 
The function checks if there are any two elements in the list that are closer than the given threshold. If there are any such general elements are closer than the threshold, the function returns True. If the loop completes and no such suitable pair is found, the function returns False.