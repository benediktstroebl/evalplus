```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    """
    return any of the numbers in the list are closer than the threshold, return True
    """
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] <= threshold:
                return True
    return False
``` 
This function works by looping through each pair of numbers in the list and checking if their sum is less than or equal to the given threshold. The two numbers are considered to be closer to each other than the threshold and the function returns True.