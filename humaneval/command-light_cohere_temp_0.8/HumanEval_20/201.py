Here's the solution:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Initialize the first and second closest values with the first two elements in the list
    first, second = numbers[0], numbers[1]
    # Sort the list based on the criteria: keep the first element and sort the rest
    sorted_numbers = sorted([first, second] + numbers[2:], key=lambda x: x[0])
    # Extract the first and second closest values from the sorted list
    return sorted_numbers[0], sorted_numbers[1]
```
This script defines a function `find_closest_elements` that takes a list of numbers and returns the first and second closest elements in the list. It accomplishes this process this selecting the element by iterating over the list and comparing each pair, until it reaches a maximum length. The script uses the list comprehension to sort the list and uses the `key` argument to sort it based on the first element of each pair. The script then extracts the elements from the sorted list and returns them as the result.