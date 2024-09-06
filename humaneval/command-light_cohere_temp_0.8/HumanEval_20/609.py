```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Create a tuple to hold the two closest numbers
    closest_numbers = (numbers[0], numbers[1])
    # Sort the list of numbers based on a custom comparator
    numbers.sort(key=lambda x: (-x, -1), reverse=(True, False))
    # Check if the lengths of the two sorted lists are even
    if len(numbers) % 2 == 0:
        # Pop the first element from the list and sort the remaining elements
        numbers = numbers[1:] + [numbers[0]]
        numbers.sort(key=lambda x: (-x, -1), reverse=(True, False))
    else:
        # Pop the last element from the list and sort the remaining elements
        numbers = [numbers[0]] + numbers[1:]
        numbers.sort(key=lambda x: (-x, -1), reverse=(True, False))
    # Reverse the order of the elements to maintain the original order of the larger number
    return numbers[0], numbers[1]
```
The function returns a tuple of two floating-point numbers, representing the two closest elements in the list.