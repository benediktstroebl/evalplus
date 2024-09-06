```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    Returns a tuple containing the two closest elements from the list, and their relative order (smaller first).
    numbers = sorted(numbers, key=lambda x: x[0]))
    return (numbers[0], numbers[1])
```
This function takes a list of numbers and sorts them in ascending order based on their first elements using the sorted() function and a lambda function. Then the function returns thes the list indices 0 and 1 to get the two closest elements and returns them as a tuple.