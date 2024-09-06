Here is a Python script that contains a self-contained function that solves the problem:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Initialize the first and second closest values
    first, second = -float("inf"), float("inf")
    for i in range(len(numbers) - 1):
        current = numbers[i]
        if current < first:
            first = current
        elif current < second:
            second = current
    else:
        return first, second
    return first, second
```

This function takes a list of numbers as input and returns a tuple of the two closest elements in the list. It uses a Python's list comprehension and a for loop to iterate through the list and find the two closest elements.  The also maintains two variables, `first` and `second`, which are initialized with the smallest and largest possible floating numbers, respectively. It then compares each element in the list with these variables and updates the values of `first` and `second` if necessary.  The two variables are updated to the elements that are closest to each other.