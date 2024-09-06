Here's a solution:
```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers
    numbers.sort(numbers, key=lambda x: (-x, 1))
    # Get the first and second smallest numbers
    first, second = numbers[0], numbers[1]
    # Return the two numbers in order of smaller number, larger number
    return (first, second)
```

The function find_closest_elements takes a list of numbers and returns a tuple of two closest numbers. The function uses the sorting algorithm to sort the list of numbers based on their values, and then selects the first and second smallest numbers. The function then returns the first and second values.