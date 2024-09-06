Here's a self-contained Python function that solves the problem:
```python
from typing import List
def find_closest_elements(numbers: List[float]):
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements")
    else:
        # Sort the list in ascending order
        sorted_numbers = sorted(numbers)
        # Initialize variables
        closest1 = sorted_numbers[0]
        closest2 = sorted_numbers[1]
        # Compare the elements and update the closest variables
        for i in range(1, len(sorted_numbers)):
            # Calculate the difference between the current element and the closest elements
            current = sorted_numbers[i]
            closest1 = min(current - closest1, closest2 - current)
            closest2 = min(current - closest1, closest2 - current)
        return closest1, closest2
```
This function takes a list of numbers as input and returns a tuple of the two closest elements. It performs a use the checked inputs to make sure the list contains at least two elements. The function then sorts the values in the list and compares the current number with the other elements. It then updates the use min function to find the closest elements in the list.

This function is self-contained, as it does not rely on any other functions or modules and can be used directly in other scripts or modules.