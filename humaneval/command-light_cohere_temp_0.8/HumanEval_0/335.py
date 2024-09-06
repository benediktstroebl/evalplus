Here's a self-contained Python script with a function that checks if any two elements in a list are closer than a given threshold:

```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    :type numbers: List[float]
    :type threshold: float  
    return any(abs(n1 - n2) <= threshold for n1, n2 in zip(numbers))
```
This function takes two inputs: a list of numbers and a threshold value. It returns True to check if any two numbers in the list are closer than the given threshold. The function uses the Python's built-in function `abs` to get the absolute value of each number, and then checks if the absolute difference of each pair is less than or equal to the threshold value.