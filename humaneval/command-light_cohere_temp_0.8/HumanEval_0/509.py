Here is a self-contained Python function that solves the problem:

```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # Sort the list of numbers
    numbers.sort(key=lambda x: (x<threshold or x>threshold))
    # return the list is sorted or not
    return numbers[-1] == numbers[0]
```

This function takes in a list of numbers and a threshold as input, and returns a boolean indicating whether the list has been sorted or not. The function sorts the list of numbers using the sort method with a lambda function. It compares the list first element with the last element, and returns True if they are equal, False otherwise. This is the same approach, as it does not use any built-in functions and only uses Python's list and comparison operators.