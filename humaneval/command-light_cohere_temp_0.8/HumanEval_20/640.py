```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Initialize a tuple to store the two closest elements
    closest1, closest2 = (float('inf'), float('-inf'))
    
    # Sort the list of numbers and store the two closest in the tuple
    for i in range(len(numbers)):
        if numbers[i] < closest1 + closest2:
            closest1, closest2 = numbers[i], closest2
    
    # Return the tuple of the two closest elements
    return closest1, closest2
```
This function, "find_closest_elements," takes a list of numbers and returns a tuple of two closest elements in the list, based on their order of magnitude. The function sorts the lowest number from the input list into the first position and the second position of the second closest number. 

This function is a good starting point for solving the problem and can be easily modified to fit the specific requirements of the problem.