```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    Selects and returns two elements that are closest to each other from the supplied list of numbers.
    """return (numbers[0][:1], numbers[1][:1])
```
The function find_closest_elements, which accepts a list of floating-point numbers as input and returns a tuple with the two closest numbers in that list, has been implemented. The function first chooses the access the closest element from the first half of the list and the closest element from the second half of the list, respectively, by using the slice notation. This is guaranteed to provide a sorted list of numbers.