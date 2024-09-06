```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Ensure length is at least 3
    if len(numbers) < 3:
        return None, None
    # Sort the list of numbers in ascending order
    numbers.sort(key=lambda num: -num)
    # Initialize the first and second closest elements with the first and last elements of the sorted list
    first, second = (numbers[0], numbers[-1])
    # Search for the remaining closest elements
    for i in range(1, len(numbers)-2):
        current = numbers[i]
        for j in range(i+1, len(numbers)):
            current = (current, nums[j])
            if current > first and current < second:
                first, second = current
    return first, second
``` 
This function takes a list of floating-point numbers and returns a tuple of the two closest numbers. It uses the type hints to ensure the list is of at least length three and then sorts the list in ascending order based on the absolute value of the numbers. The function then uses a binary search to find the remaining closest elements after the first and second closest elements have been initialized with the first and last elements of the sorted list.