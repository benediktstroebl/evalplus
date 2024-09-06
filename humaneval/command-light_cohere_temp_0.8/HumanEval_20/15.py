```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Initialize the first and second closest distances as infinity
    first_closest, second_closest = (float("inf"), float("inf"))
    
    # Compare numbers to find the first and second closest values
    for i in range(len(numbers)):
        if numbers[i] < first_closest[0]:
            first_closest[1] = numbers[i]
        elif numbers[i] > second_closest[0]:
            second_closest[1] = numbers[i]
        else:
            first_closest[0] = numbers[i]
            second_closest[0] = numbers[i]
    
    # Return the two closest values in order
    return first_closest[0], second_closest[0]

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]

result = find_closest_elements(numbers)
```
The function "find_closest_elements" takes a list of numbers as input and returns a tuple containing the two closest values. The function works by initializing the first and second closest distances as infinity, and then comparing each number in the list to the current closest values to find the two closest values. 

The function then updates the first and second closest distances accordingly until it finds the two closest values. The function then returns the result, which is the two closest values in order.

This is a self-contained function, and it can be used to solve the problem of finding the two closest values in a list of numbers.