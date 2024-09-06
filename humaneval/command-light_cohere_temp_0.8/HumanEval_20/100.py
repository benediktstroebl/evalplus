Here is a self-contained Python script with a self-contained function that solves the problem:
```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """ Returns a tuple containing the two closest numbers in the list and their order """
    closest1 = float('inf')
    closest2 = float('-inf')

    for num in numbers:
        # Calculate the difference between the current number and the two closest numbers
        diff1 = abs(num - closest1)
        diff2 = abs(num - closest2)

        # Check which difference is smaller
        if diff1 < diff2:
            closest1 = num
            closest2 = num
        elif diff2 < diff1:
            closest2 = num
            closest1 = num

    return closest1, closest2

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
numbers to select the two closest elements.
```