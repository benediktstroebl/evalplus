```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Initialize the first and second closest variables
    first, second = 0.0, 1.0
    
    # Initialize the+/1 and the previous closest pair variables
    closest_pair = (first, second)
    
    # Loop through the list of numbers and find the smallest in the current pair, and update the variables
    for num in numbers:
        if num < first:
            first = num
        if num < second:
            second = num
        if first == second:
            # If this is the first time to find a pair, return it
            if closest_pair[0] == 0.0:
                return (first, second)
            # Else, update the pair
            closest_pair = (first, second)
    
    return closest_pair

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]
return find_closest_elements(numbers)[0]
```