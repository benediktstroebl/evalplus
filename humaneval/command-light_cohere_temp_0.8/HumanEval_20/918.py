Here is a self-contained Python script that includes a function that solves the problem of finding the two closest elements in a list of numbers:
```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each other and return them in order (smaller number, larger number).
    # Sort the list to make it easier to find the closest elements
    sorted_numbers = sorted(numbers)
    # Get the first and last elements in the sorted list
    first_element = sorted_numbers[0]
    last_element = sorted_numbers[-1]
    # Now we have the first and last elements of the sorted list, we can find the closest pair
    first_index = -1
    last_index = -1
    # Start at the beginning and end of the sorted list
    for index in range(len(sorted_numbers)):
        if sorted_numbers[index] > first_element:
            # If the current element is larger than the first element, we found our first element
            first_index = index
            break
        if sorted_numbers[index] > last_element:
            # If the current element is larger than the last element, we found our last element
            last_index = index
            break
    # If we didn't find the first or last element, it means that there is no pair of closest elements.
    if first_index == -1 or last_index == len(sorted_numbers) - 1:
        return (sorted_numbers[first_index], sorted_numbers[last_index])
    # If we found the first and last elements, return them
    return (first_element, last_element)
```
The function takes a list of numbers as input and returns a tuple of the two closest elements in the list, with the smaller number first. The function uses a sorting the list of numbers and then uses the first and last elements to find the two closest elements. The function also handles the case where there is no pair of closest elements, and returns the first and last elements of the list.