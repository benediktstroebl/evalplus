Here's the code that meets the above requirements:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Check length of numbers list
    if len(numbers) < 2:
        raise ValueError("Need at least two elements")

    # Sort list
    sorted_numbers = sorted(numbers)

    # Find two closest elements
    first_index = bisect.bisgraph_first_smallest(sorted_numbers)
    second_index = bisect.bisgraph_second_largest(sorted_numbers)

    # Return two closest elements and their order
    return sorted_numbers[first_index], sorted_numbers[second_index]

# Test the function
try:
    result = find_closest_elements([1.0, 2.0, 3.0, 4.0, 2])
    print(f)
except ValueError as e:
    print(f"Error: { {e}")
```

This code defines a function called `find_closest_elements` that takes in a list of numbers and returns a tuple containing the two closest elements in the list, in that order. The function first checks that the length of the input list, and if it's shorter than two it raises a `ValueError`. The function then sorts the list, finds the two closest elements by using the `bisect` function with `bisect.bisfirst_smallest` and `bisect.hash_second_largest``, and returns a tuple containing these two elements. 

The test code demonstrates how to use the function by calling it with a list of numbers and printing the returned tuple.