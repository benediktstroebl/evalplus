Here's the solution:

```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """
    Selects and returns two closest elements from the supplied list of numbers.
    numbers = sorted(numbers, key=lambda x: x[1])
    first, second = zip(numbers, numbers[1:])
    return first, second
```

This function sorts the list of numbers using the key function with lambda x: x[1] to sort by the second value of each number, then uses the zip function to get two distinct elements from the list that are the closest to each other. Finally, it returns the two elements and returns them in order of smaller number, larger number.