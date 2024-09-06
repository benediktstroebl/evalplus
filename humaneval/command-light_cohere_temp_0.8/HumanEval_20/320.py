Here is a Python script that contains a self-contained function that solves the problem of finding the closest two elements in a list of numbers:
```python
import math

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each other and return them in order (smaller number, larger number).
    ```
    # Sort the list of numbers in descending order
    sorted_numbers = sorted(numbers, reverse=True)

    # Initialize variables
    closest1 = None
    closest2 = None

    # Loop through the list and find the two closest numbers
    for num in sorted_numbers:
        if closest1 is None or num < closest1:
            closest1 = num
        elif num < closest2:
            closest2 = num

    # Return the two closest numbers
    return (closest1, closest2)

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]

result = find_closest_elements(numbers)

The function find_closest_elements takes a list of numbers and returns a tuple containing the two closest numbers. The function first sorts the numbers in descending order and then loops through the list, finding the two closest numbers. The function then returns the closest2 and closest1, which are the two numbers that are the closest to each other in the list.