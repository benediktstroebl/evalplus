Here's the solution:

```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Initialize the first and second closest elements
    first, second = (min(numbers), max(numbers))[0]
    # Loop through the numbers, and as long as the current number is closer to the first or second closest element, update which is the first or second closest element
    while first <= numbers[0] <= second and numbers[1] <= numbers[0] <= second:
            if numbers[0] == first:
                first = numbers[1]
            else:
                second = numbers[0]
    return first, second
```

This function takes a list of numbers and returns two values: the first is the closest to the second closest element and the second is the other closest number. It loops by initializing the the first and second closest element to start the comparison. The while the current number is within the range defined by the first and second closest element, it compares the current number with the first and second numbers and updates which is the first and second closest element.