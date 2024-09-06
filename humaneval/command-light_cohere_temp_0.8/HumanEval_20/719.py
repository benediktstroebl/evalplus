```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Take the first element of the list
    x = numbers[0]
    # Sort the list in ascending order
    sorted_numbers = [num for num in numbers if num != x] + [x]
    # Take the first two elements of the sorted list
    y = sorted_numbers[1]
    # Return the two numbers in descending order
    return (y, x)
```