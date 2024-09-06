```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """
    Returns a tuple containing the two numbers with the smallest and largest values in the list.
    """
    list indices = list(range(len(numbers)))
    smallest = float('inf')
    largest = float('-inf')
    for i, num in enumerate(numbers):
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    return smallest, largest
```
This function takes a list of numbers as input and returns a tuple containing the two numbers with the smallest and largest values in the list.

The function first creates a list of indices of the list to iterate through. Then, it creates two variables, `smallest` and `largest`, to keep track of the smallest and largest values in the list. The function then iterates through the list of indices and assigns the smallest and largest values in the list to the `smallest` and `largest` variables.

Finally, the function returns the `smallest` and `largest` values, which are the two numbers that are the closest to each other in the list.