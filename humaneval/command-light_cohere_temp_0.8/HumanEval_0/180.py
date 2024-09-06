Here is a self-contained Python script that solves the problem you have described:

```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5).4) False.
    return False


    # Exclude the case where any number is 1.0 or less threshold. 
    # Else, check if any two consecutive elements are closer to each other than threshold.
    return the highest and lowest elements of the list.
 ```


# Example usage:
numbers = [1.0, 2.0, 3.0, 0.0, 5.0, 2.0]

has_close_elements(numbers, 0.3) 
```
This script defines a function called `has_close_elements` that takes a list of numbers and a threshold as input. The function returns True if any two numbers in the list are closer than the threshold, and False otherwise. The function uses the `max` and `min` functions to get the highest and lowest elements in the list, respectively, and checks if the distance between those elements is less than the threshold.