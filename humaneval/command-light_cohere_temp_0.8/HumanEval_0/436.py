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
The function returns True if any two numbers in the list are closer than the threshold, otherwise False. The function uses a loop to iterate over the list and the function returns True if any two numbers are closer than the threshold.