Here is the code:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Using default parameter values to make the function signature more readable
    # Convert the list of numbers into a tuple of (distance, element) pairs
    distances, elements = zip(numbers)
    # Sort the list of tuples based on their first element
    sorted_elements = sorted(zip(numbers), key=lambda x: x[0]))
    # Extract the two closest elements from the sorted list
    closest_elements = sorted_elements[:2]
    return closest_elements

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]

result = [0.02, 2.0]
```

This code defines a function **find_closest_elements** that takes a list of numbers and returns a tuple containing the two closest elements. The function uses the sorting algorithm to find the two closest elements, and then returns them in order of their smaller value.