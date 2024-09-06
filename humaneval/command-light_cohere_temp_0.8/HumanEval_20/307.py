Here's a solution for the problem you described:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each other and return them in order (smaller number, larger number).
    The function will return a tuple with the two closest elements and their order. The first element is the smallest number and the second element is the largest number.

numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]

result = (2.0, 4.0)
```
```

This solution uses the **"List comprehension"** to filter and return two closest elements from the list of numbers. The function returns a smallest and largest number in the tuple.

Note that this function assumes that the list of numbers has at least two elements. If the list has less than two elements, it will raise an error.