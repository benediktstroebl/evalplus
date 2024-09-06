Here's a self-contained Python script that solves the problem of finding the two elements in a list that are closest to each other and returns them in order:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    if len(numbers) < 2:
        return numbers, numbers  # one element is always the same as itself
    
    # Sort the list of numbers in ascending order
    sorted_numbers = sorted(numbers)
    
    # Initialize the two closest elements to the first and last elements in the sorted list
    closest1 = sorted_numbers[0]
    closest2 = sorted_numbers[-1]
    
    # Loop until the two elements are the same
    while closest1 == closest2:
        closest1 = closest1 + 1
        closest2 = closest2 + 1
    
    # Return the two closest elements in the list
    return closest1, closest2
```

The function takes a list of numbers as input and returns a tuple containing the two closest elements in the list. It uses the value of the maximum element of each pair of elements to compare and determine which element is closer to the other.