```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    Selects and returns two elements in the supplied list that are the closest to each other. The two elements are returned in ascending order of their sum (smaller number, larger number).
    return tuple(sorted([num for num in numbers if num != numbers[-1] or num != numbers[0]]))
```
This solution defines a function called `find_closest_elements` that takes a list of numbers as input and returns a tuple containing the two elements in the list that are the closest to each other. The function uses the sorting algorithm based on the sum of the elements and selects the elements in ascending order.