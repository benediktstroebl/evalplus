```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers
    numbers.sort(numbers)
    
    # Determine the smallest and largest numbers
    smallest = numbers[0]
    largest = numbers[-1]
    numbers.remove(smallest)
    numbers.remove(largest)

    # Find the two closest numbers
    closest_numbers = numbers[:2]
    return _find_closest_elements(numbers[1:]), (smallest, largest)

def _find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ Return the closest pair of floating-point numbers in the input list.

    # Sort the first half of the list
    sorted_numbers = sorted(numbers)

    # Determine the smallest and largest numbers
    smallest = sorted_numbers[0]
    largest = sorted_numbers[-1]
    # Remove the largest number from the list to ensure that the largest number is returned
    # in the pair with the smallest number
    numbers.remove(largest)

    # Return a tuple containing the smallest and largest numbers in reversed order
    return (largest, smallest)

# Example:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
result = find_closest_elements(numbers)
 ```

This Python script defines a function called `find_closest_elements` that takes a list of floating-point numbers as input and returns a tuple containing the two closest numbers in the list, along with their relative difference. The function first sorts the smallest and largest numbers in the list and then removes the largest number to ensure that it is not returned as part of the closest pair. 

The function then returns the result of a helper function `_find_closest_elements`, which sorts the remaining numbers, determines the smallest and largest numbers, and returns the closest pair of numbers in reversed order.