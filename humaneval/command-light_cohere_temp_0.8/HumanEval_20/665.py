Here is the solution for the problem you provided:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ Returns the two closest elements in the list, in order of the smaller number, and returns them as a tuple.

    A tuple containing the 1) the closest smaller element and 2) the closest larger element.

    # Sort the 0 to last by value
    sorted_numbers = sorted(numbers)

    # Get the first two elements in the sorted list
    first_small = sorted_numbers[0]
    first_large = sorted_numbers[1]

    # Return the two closest elements in the list
    return (first_small, first_large)

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]

result = find_closest_elements(numbers)
```

The function first sorts the list of numbers, then extracts the first two numbers. Then, the function returns the two numbers and returns them as a tuple. The function uses the tuple unpacking to return the two numbers in the correct order.