```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers in ascending order
    sorted_numbers = sorted(numbers)
    
    # Initialize variables
    first = None
    second = None
    
    # Search for the smallest and largest number in the sorted list
    for i, num in enumerate(sorted_numbers):
        if first is None or num < first:
            first = num
        elif second is None or num > second:
            second = num
    
    # Return the smallest and largest number in the list
    return Tuple(first, second)

# Example of passing the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print_closest_elements(numbers)
```