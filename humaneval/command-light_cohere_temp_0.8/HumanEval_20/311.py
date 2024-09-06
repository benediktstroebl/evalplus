```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Initialize variables to compare
    first = numbers[0]
    second = numbers[1]

    # Check the distance between the elements
    dx = abs(first - second)

    # If the distance is smaller than the specified value, assign the second element as the current first
    if dx < numbers[2]:
        first = second
        second = numbers[0]

    # Return the two elements in order
    return (first, second)

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print_closest_elements(numbers)
``` 
This script defines a function called **find_closest_elements** that takes a list of floating-point numbers as input and returns a tuple containing the two closest elements in the list, along with their relative difference.

The function uses a comparison-based approach to find the two closest elements and returns them in order.