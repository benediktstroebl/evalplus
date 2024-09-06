Here is a self-contained Python script that solves the problem of finding the closest elements from a supplied list of numbers:
```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers
    numbers.sort_numbers = sorted(numbers)
    # Initialize the first and second variables
    first, second = numbers[0], numbers[1]
    # Return the two closest numbers in the list
    return (first, second)

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]
result = find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2])
return (2.0, 3.0)

```
This script defines a function, `find_closest_elements`, that takes a list of numbers as input and returns a tuple containing the two closest numbers in the list, which are then returned in order of their closeness.