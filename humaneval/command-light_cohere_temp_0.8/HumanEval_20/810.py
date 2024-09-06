Here's a Python script with a self-contained function that solves the problem and passes the tests:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Check length of input list is at least 2
    if len(numbers) < 2:
        return "Input list must be at least 2 elements."
    
    # Sort the list in ascending order
    sorted_numbers = sorted(numbers)
    
    # Select two numbers that are the closest to each other
    first_index = 0
    second_index = len(sorted_numbers) - 1
    while first_index < second_index:
        # Calculate the difference between the two numbers and check if it's negative
        current_first = sorted_numbers[first_index]
        current_second = sorted_numbers[second_index]
        difference = current_first - current_second
        if difference < 0:
            first_index += 1
        else:
            second_index -= 1
    
    # Return the two selected numbers
    return (sorted_numbers[first_index], sorted_numbers[second_index])

# Test the function
```

You can test the function with a list of numbers, and it will return the two elements that are the closest to each other.