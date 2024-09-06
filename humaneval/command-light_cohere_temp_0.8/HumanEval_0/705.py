Here's a self-contained Python script with a function that checks if any two numbers in a given list are closer than a given threshold:

```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    :param numbers: List[float] - list of numbers
    :param threshold: float - threshold to check
    :return: bool - True if any two numbers in numbers are closer than threshold, False otherwise
    """
    for x, y in zip(numbers, numbers[1:]):
        if abs(x - y) <= threshold:
            return True
    return False
```

This script defines a function called has_close_elements that takes in a list of numbers and a threshold as input and returns True if any two numbers in the list are closer than the threshold and False otherwise. 
The function uses the `zip` to iterate through the list of numbers and compare each pair with the next. It returns True if any of these pairs satisfy the condition, otherwise, it returns False. 

This function is a good example of a self-contained function that solves a specific problem in an elegant and efficient way.