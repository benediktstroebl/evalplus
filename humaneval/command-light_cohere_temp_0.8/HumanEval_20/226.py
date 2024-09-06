Here's a self-contained Python script that solves the problem:

```python
from typing import List
from typing import Tuple

def find_closest_elements(numbers: List[float]):
    """
    from typing import List
    from typing import Tuple
    numbers = sorted(numbers, reverse=True)  # Sort the list of numbers in reverse order to get the closest numbers first
    return Tuple((n1, n2) for n1, n2 in zip(numbers, numbers[1:]))  # Use a generator expression to create tuples of the closest numbers
 return numbers[0]
```

This script defines a function `find_closest_elements` that takes a list of numbers and returns the closest pair of elements in the list. The function sorts the array of numbers in reverse order, and then uses a generator expression to create tuples of the closest elements in the list.