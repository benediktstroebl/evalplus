Here's the solution:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers in ascending order
    sorted_numbers = sorted(numbers)

    # Initialize the variables
    closest1, closest2 = (sorted_numbers[0], sorted_numbers[1])

    # Compare the two elements and update the variables
    while closest1[0] < closest2[0]:
        closest1 = (closest1[0] + 1, closest1[1] + 1)
        closest2 = (closest2[0] + 1, closest2[1] + 1)

    # Return the two closest elements
    return closest1, closest2
```
The provided code defines a function called `find_closest_elements`, which takes a list of numbers as input and returns a tuple containing the two closest numbers. 

This function first sorts the list of numbers in ascending order. Then, it initializes two variables, `closest1` and `closest2`, with the first and second elements of the sorted list. 

The code then enters a loop, comparing the two variables and updating them until one of the numbers reaches the other. Finally, the function returns the two closest elements as the result.