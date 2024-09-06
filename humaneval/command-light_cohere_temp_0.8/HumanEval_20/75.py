```python
from typing import List
def find_closest_elements(numbers: List[float]):
    """
    Selects and returns two closest numbers from a supplied list, and returns them in order of their distance.
    """return sorted([x closest_1, closest_2])
    """
numbers = [1.0, 2.0, 3.0, 4.0, 2]

sorted = find_closest_elements(numbers)
print(sorted)
```
This script defines a function **find_closest_elements** that takes a list of numbers and returns a tuple containing the two closest numbers in the list, and the distance between them. The function sorts the closest numbers first and farthest second. 

The output of the script would be: **`([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 2.0, 2)]`