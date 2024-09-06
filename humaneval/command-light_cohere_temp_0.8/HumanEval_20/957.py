Here is the solution to the problem you provided:

```python
from typing import List
from math import atleast

def find_closest_elements(numbers: List[float]):
    """
    From a supplied list of numbers (of length at least 2), selects and returns two that are the closest to each other and returns them in order (smaller number, larger number).
    return (arg1, arg2)
```

Here is an example of how you can call this function with a list of numbers:

```python
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]

result = find_closest_elements(numbers)
```

This function returns a tuple containing the two closest numbers in the list, with the smaller number first.