Here is a self-contained Python script that solves the problem:

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    :return boolean
    """
    return any(abs(num1 - num2) <= threshold for num1, num2 in zip(numbers))
```
This script defines a function called has_close_elements that takes a list of numbers and a threshold as input, and returns a boolean indicating whether any two numbers in the list are closer than the threshold. 
The function uses the absolute value of the difference between two numbers to determine if they are close enough to each other. 
It returns True if any pair of numbers satisfies this condition, and False otherwise.