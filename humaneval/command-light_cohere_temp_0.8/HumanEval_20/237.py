Here's the solution:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers
    numbers.sort(numbers)
    
    # Take the first and second elements
    first, second = numbers[0], numbers[1]
    
    # Return the elements in order, smaller number first
    return (first, second)
```
This function takes a list of numbers as input and returns a tuple of the two numbers that are closest to each other. The function first sorts the dry numbers and then takes the first and second elements from the sorted list.