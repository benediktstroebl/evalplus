```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers
    numbers.sort(numbers, key=lambda n: -n)
    # Get the first two elements of the sorted list
    # that are closest to each other.
    first_element = next(numbers, default=[])[0]
    second_element = next(numbers, default=[])[1]
    # Return the two elements in order (smaller number, larger number)
    return first_element, second_element

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]

result = find_closest_elements(numbers)
```

This code defines a function called `find_closest_elements` that takes a list of numbers as input and returns a tuple containing the two elements in the list that are the closest to each other. The function first sorts the list of numbers, then uses the `next` function with a default argument to get the first and second closest elements from the sorted list. The function then returns these elements in order, smaller number, larger number.