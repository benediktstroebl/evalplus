```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise IndexError("List of numbers must have a minimum of two elements")
    else:
        return (numbers[0], numbers[-1])
```

This script sorts a list of numbers and then returns the two closest numbers at each end of the sorted list. It raises an error if the list length is less than 2. This solution is complete and should work as expected for the given problem.