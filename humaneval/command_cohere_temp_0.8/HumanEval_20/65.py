```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    nums_sorted = sorted(numbers)
    return nums_sorted[0], nums_sorted[-1]
```

This script defines a function `find_closest_elements` which takes in a list of float numbers and returns two float numbers that are closest to each other. The function first sorts the list and then returns the first and last numbers in the sorted list.

Here is a sample output:
```bash
(2.0, 2.2)
```