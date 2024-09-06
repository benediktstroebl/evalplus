```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    Return True if at least one pair of numbers in the list are closer than the threshold
    Otherwise return False
    """
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] - numbers[j] < threshold:
                return True
    return False
``` 

This function uses a nested loop to iterate over the list of numbers and compare each pair of elements. It returns True if at least one pair of numbers are closer than the threshold. 

This function is a self-contained solution and can be easily integrated into a markdown code block to solve the problem.