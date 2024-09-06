```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Initialize closest and second variables
    closest, second = float('inf'), float('-inf')
    # Loop through list
    for num in numbers:
        # Compare and update closest and second variables
        if num < closest:
            second = closest
        closest = num
    # Return ordered closest and second values
    return (closest, second)
```
This code defines a function called **find_closest_elements** that takes in a list of numbers as input and returns a tuple of the closest and second closest numbers in the list.