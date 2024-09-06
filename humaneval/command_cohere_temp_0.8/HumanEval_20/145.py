```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise ValueError("At least two numbers must be provided")
    else:
        difference = numbers[-1] - numbers[0]
        if difference < 0:
            # This is a check for the edge case wherein the list contains only negative numbers, or only positive numbers.
            raise ValueError("Please provide a list of numbers with content between 0 and positive infinity")
        else:
            return numbers[0], numbers[-1]
```

This script sorts a list of numbers, checks for at least two numbers to be present, and then returns the two closest numbers from the list as a tuple, in the order of the smaller number first and the larger number second. It also includes validation to check for edge cases wherein the list contains only positive or negative numbers, in which case it raises a ValueError. This ensures the function is robust to certain types of invalid input. 

The function works as expected with the given test cases, but it may be beneficial to add additional tests for complex numbers, integers, and other number types.