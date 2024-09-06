Here's a self-contained Python script that solves the problem:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers
    numbers.sort(numbers)

    # Select the two closest numbers
    closest1 = min(numbers, key=numbers.get('2'))
    closest2 = max(numbers, key=numbers.get('2'))
    return (closest1, closest2)

# Test case
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(find_closest_elements(numbers))
```
The function `find_closest_elements` in this script accepts a list of numbers as an argument. It sorts the list and returns a tuple with the two closest values. It utilizes the min and max functions to determine the two closest values and returns them in that order. The test case at the end demonstrates how to utilize the function.

The function runs independently, without requiring external data or other functions, and may be used to solve the problem for any given list of numbers.