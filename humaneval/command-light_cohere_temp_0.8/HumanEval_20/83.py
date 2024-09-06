Here is a Python script that contains a self-contained function to solve the problem:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    #type: Tuple[float, float]
    # Initialize the first and second closest numbers as the first and last numbers in the list.
    first, second = numbers[0], numbers[-1]
    if len(numbers) < 2:
        return first, second
    # Sort the list by the numbers in descending order
    sorted_numbers = sorted(numbers, reverse=True)
    # Search the first and second closest numbers in the sorted list
    first, second = sorted_numbers[0:1]
    return first, second
```

This script defines a function called `find_closest_elements` that takes a list of numbers as input and returns a tuple of the two closest numbers in the list. The function first sorts the initializes the first and second closest numbers, and then searches the first and second closest numbers in the sorted list to return them as the final output.