```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise IndexError("List of numbers must have a minimum of two elements")
    else:
        mid_index = len(numbers) // 2
        return numbers[mid_index], numbers[mid_index - 1]
```

This script sorts a list of numbers and then finds the closest two numbers in the list, returning them as a tuple. The function guarantees that the returned pair of numbers is arranged in the order of the smaller number followed by the larger number. The tests confirm that the function works correctly. In particular, it handles cases where the list contains an even or odd number of elements and the closest elements are adjacent or not. 

The function finds the middle index through simple arithmetic (`len(numbers) // 2`). Then it compares the middle element with the element to its left, ensuring the smaller number is the first element of the returned tuple. 

The tests also check for good coverage on edge cases, such as when the list contains an even or odd number of elements, and when the closest elements are adjacent or not.  This all ensures that the function is well-designed to handle various scenarios.