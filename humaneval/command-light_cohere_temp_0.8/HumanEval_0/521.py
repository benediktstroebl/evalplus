```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] - numbers[j] < threshold:
                return True
    return False
``` 
This function takes two parameters: numbers, which is a list of floating-point numbers, and threshold, which is a float that specifies the minimum distance between any two numbers in the list. It then returns a return True, which is a boolean that indicates whether any two numbers in the list are closer to each other than the threshold.