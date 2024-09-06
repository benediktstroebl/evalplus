```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers in ascending order
    sorted_numbers = sorted(numbers)

    # Initialize the first and second closest elements to None
    first = second = None

    # Loop through the sorted list of numbers
    for num in sorted_numbers:
        if first is None or num < first:
            second = first
            first = num
        elif num < second:
            second = num

    # Return the first and second closest elements
    return (first, second)

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]

result = find_closest_elements(numbers)
```

This function, find_closest_elements, takes a list of numbers as input and returns a tuple containing the two closest numbers. It sorts the names for the first and second closest elements, respectively. This method allows you to easily distinguish between the two closest elements and return them in the order of closest to farthest. 

Note: This code assumes that the list of numbers is provided as input and is not empty. The code also uses the type hint for List and Tuple, which are necessary for working with lists of elements.