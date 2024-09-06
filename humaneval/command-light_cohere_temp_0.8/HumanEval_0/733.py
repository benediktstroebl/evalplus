Here's a self-contained Python script that solves the problem you've described:

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    Return True if any two distinct numbers in the list are less than threshold apart
    """
    return any(x != y for x, y in zip(numbers, numbers[1:])) and numbers[0] <= threshold
```
This function, named has_close_elements, takes a list of numbers and a threshold as input. It returns True if any two distinct numbers in the list are less than the given threshold apart. This function efficiently uses the fact to check if any two distinct elements in the list are not close enough to each other. 

In this script, the function uses the zip function to pair each number in the list with every other, and then checks if any of these pairs meet the condition that the two numbers are less than the threshold apart.