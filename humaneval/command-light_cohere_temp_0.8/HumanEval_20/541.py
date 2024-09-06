Here's the Python code snippet:
```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Define the function
    closest1, closest2 = float('inf'), float('-inf')
    # Sort the list of numbers in ascending order
    sorted_numbers = [num for num in numbers if num not in [closest1, closest2]] + [closest1, closest2]
    sorted_numbers.sort()
   10.move_to_closest_elements()
    # Return the two closest numbers in the list
    return sorted_numbers[0:2]
```

The function `find_closest_elements` takes a list of numbers and sorts the list based on the ascending order of the numbers, then returns the two closest numbers in the list. This is two numbers are returned in the order of smaller number to larger number.