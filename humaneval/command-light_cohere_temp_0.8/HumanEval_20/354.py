Here is a Python script that solves the problem of finding the two elements in the list that are closest to each other:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each other and return them in order (smaller number, larger number).

    Parameters:
        numbers: List[float] - list of floating-point numbers to find closest elements for

    Returns:
        Tuple[float, float] - two floating-point numbers that are the closest to each other and in order, with the smaller number first
    """
    numbers = sorted(numbers)
    # Extracting the first and last elements from the sorted list
    first_element = numbers[0]
    last_element = numbers[-1]
    # Starting from the first and last elements, iterating until the second element is found
    while first_element != last_element:
        # Swapping the first and last elements and moving to the second element
        temp = first_element
        first_element = last_element
        last_element = temp
        # Checking if the second element has been found
        if first_element == last_element:
            break
        # continue the loop
        temp = last_element
        last_element = first_element
    return first_element, last_element
```

This function takes a list of numbers and returns a tuple of two floating-point numbers that represent the two elements in the list that are the closest to each other. The function sorts the the list of numbers, and then uses the first and last elements of the sorted list to find the two elements that are closest to each other. The function then continues to the loop, swapping the first and last elements, until the second element is found. The function then returns the final result of the two closest elements.

This is a simple example of how you can use Python to solve a problem involving finding the closest elements in a list.