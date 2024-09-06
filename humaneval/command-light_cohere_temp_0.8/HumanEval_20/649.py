```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers in ascending order
    sorted_numbers = sorted(numbers)

    # Initialize variables to track the first and second closest elements
    first_closest, second_closest = (sorted_numbers[0], sorted_numbers[1])

    # Compare the first and second closest elements
    if sorted_numbers[0] < sorted_numbers[1]:
        first_closest, second_closest = (sorted_numbers[1], sorted_numbers[0])
    else:
        first_closest, second_closest = (sorted_numbers[0], sorted_numbers[1])

    # Return the first and second closest elements
    return first_closest, second_closest

# Sample usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]
0]
first, second = find_closest_elements(numbers)
print(f"First: {first}")
print(f"Second: {second}")
```
This script defines a function called `find_closest_elements` that takes a list of numbers as input and returns a tuple containing the two closest elements in the list, in that order. It does this by sorting the list of numbers, and then comparing the first and second closest elements to determine which is the smaller number. The script also uses the nesting to create variables that hold the first and second closest elements.

This function can be used to solve the problem of finding the closest elements in a markdown code block, and the result can be printed to the console.