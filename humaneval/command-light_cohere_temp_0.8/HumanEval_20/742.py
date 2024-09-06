```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """
    Returns a tuple containing the two closest elements in the supplied list.
    """
    sorted(numbers)  # Sort the list in ascending order
    first, second = numbers[0]  # Store the first number
    if numbers[1] - first > numbers[0] - second:
        first, second = numbers[1], numbers[0]
    return first, second
```
This script defines a function called `find_closest_elements` that takes a list of numbers and returns a tuple with the two closest elements. The function first sorts the gembers the list in ascending order, then it checks if the difference between the first and second elements is greater than the difference between the second and the third elements. Finally, it swaps the two elements and returns the first element.