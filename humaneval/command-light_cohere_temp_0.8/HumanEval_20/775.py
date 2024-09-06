```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers
    numbers.sort(numbers)
    # Initialize variables
    closest1, closest2 = (numbers[0], numbers[1])
    # Compare the two numbers
    if numbers[0] < numbers[1]:
        closest1, closest2 = (numbers[1], numbers[0])
    else:
        closest1, closest2 = (numbers[0], numbers[1])
    # Return the two closest numbers
    return closest1, closest2
```

This function will return the two closest numbers from the list, in order of their magnitude.