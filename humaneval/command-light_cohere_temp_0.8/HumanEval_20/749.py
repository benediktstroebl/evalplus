Here's a self-contained Python function that solves the problem:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers
    sorted_numbers = sorted(numbers)
    # Initialize the first and second closest numbers
    first = last = sorted_numbers[0]
    for i in range(1, len(sorted_numbers)):
        current = sorted_numbers[i]
        # If the current number is less than the first, update first and last
        if current < first:
            first = current
        last = current
    # Return the two closest numbers in order (smaller number, larger number)
    return first, last
```
This function takes a list of numbers as input and sorts the list. Then, it uses the difference of the current number and the previously stored first number to update the first and last variables. Then, it returns the two closest numbers in order of their values.