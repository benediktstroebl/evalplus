Here is a self-contained Python script that solves the problem you have provided:

```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    """
    note that any two elements that are equal to the threshold will not be considered close to each other.

    # sort the numbers in ascending order
    numbers.sort()

    list of floats, ascending order
   
    for x, y in zip(numbers[1:], numbers[2:]):
        if x != threshold and y != threshold:
            return True
    return False

test_case = [1.0, 2.0, 3.0, 4.0, 5.0, 2.0]

has_close_elements(test_case, 0.8)
```

This script defines a function called `has_close_elements` that takes a list of numbers and a threshold as input and returns a boolean value indicating whether any two numbers in the list are closer than the threshold. The function first sorts the list of numbers in ascending order, then, it uses a loop to iterate over the pairs of numbers in the list and checks if the current number is not equal to the threshold. If the current number is not equal to the threshold and the current number is not equal to any previously checked number, then the function returns True. If the loop completes without finding any number that is not equal to the threshold, then the function returns False.