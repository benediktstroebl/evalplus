Here's the solution:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the list in ascending order
    sorted_numbers = sorted(numbers)

    # Initialize variables
    smallest_number = sorted_numbers[0]
    largest_number = sorted_numbers[0]

    # Loop to find the two closest elements
    for i in range(1, len(sorted_numbers)):
        current_number = sorted_numbers[i]

        # Check if the current number is smaller than the smallest and larger than the largest
        if current_number < smallest_number and current_number > largest_number:
            smallest_number = current_number
            largest_number = current_number
        else:
            if current_number < smallest_number:
                smallest_number = current_number
            if current_number > largest_number:
                largest_number = current_number

    return smallest_number, largest_number

```

You can call this function with a list of numbers as an argument and it will return the two closest elements in the list as a tuple, in ascending order from the smallest to the largest.

Please note that this solution assumes that the list of numbers is at least two elements long. If the list is shorter than it may not function correctly.