```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    # sort the list
    numbers.sort(key=lambda x:x)
    # check if the first element is less than the threshold
    if numbers[0]<threshold:
        return False
    # check if the second element is greater than the threshold
    if numbers[-1]>threshold:
        return False
    # check if two adjacent elements are less than threshold
    if numbers[0] + numbers[-1] <= threshold:
        return False
    # return True
    return True
``` 
Do you have any other questions I can help you with?