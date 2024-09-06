Here is a Python script that contains a self-contained function that solves the problem of finding the two closest elements from a list of numbers:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers in ascending order
    sorted_numbers = sorted(numbers)
    
    # Initialize the first and second closest elements to the first and last elements in the sorted list
    first = last = sorted_numbers[0]
    
    # Initialize the remaining closest elements to the rest of the sorted list
    remaining = sorted_numbers[1:]
    
    # Loop until two elements have been found and returned
    while len(first) < 2:
        # Check if the current element is less than the last element
        if sorted_numbers[0] < sorted_numbers[len(sorted_numbers) - 1]:
            second = sorted_numbers[len(sorted_numbers) - 1]
            first.append(second)
            second = sorted_numbers[0]
        else:
            second = remaining[0]
            first = remaining.append(second)
            second = remaining[len(remaining) - 1]
    
    # Return the two closest elements in the list
    return first, second
```