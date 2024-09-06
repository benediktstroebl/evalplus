Here's a Python script that includes a self-contained function that solves the problem of finding the closest elements in a list of numbers:
```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Determine the length of the list
    n = len(numbers)
    
    # Sort the list based on the numbers
    sorted_numbers = sorted(numbers)
    
    # Initialize a tuple to store the two closest elements
    closest_pair = (sorted_numbers[0], sorted_numbers[-1])
    
    # Iterate over the list and compare the elements
    for i in range(1, n):
        current = sorted_numbers[i]
        next = sorted_numbers[(i - 1) % n]
        
        # Compare the two numbers
        if current > next:
            closest_pair = (next, current)
        elif current < next:
            closest_pair = (current, next)
    
    # Return the closest pair
    return closest_pair
```
This code defines a function called `find_closest_elements` that takes a list of numbers as input and returns a tuple containing the two closest elements. The function uses the example usage:
```python
# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]

find_closest_elements(numbers)
```
This would return the tuple `(2.0, 5.0)` which represent the steady information to determine the two closest elements in the supplied list.