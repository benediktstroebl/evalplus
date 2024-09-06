Here is a self-contained Python script that solves the problem:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    for i in range(len(numbers) - 1):
        if numbers[i] - numbers[i+1] < threshold:
            return True
    return False
``` 
This function takes two parameters: `numbers`, which is the list of numbers we want to check, and `threshold`, which is the minimum threshold that must be met for any two numbers to be considered "close". 

This function loops over the list of numbers and checks if the difference between the current number and the next number is smaller than the given threshold. If this is the condition is met, it returns `True`. If the loop completes without meeting the condition, it returns `False`. 

This code is a good example of a self-contained function, as it does not depend on any other functions and can be called directly to solve the problem.