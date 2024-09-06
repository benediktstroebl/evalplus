```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    nums_copy = list(numbers)
    closest_pair = sorted(nums_copy[:2])
    return closest_group := tuple(sorted(group)) for group in itertools.groupby(nums_copy) if len(group) > 1 else None

# Tests:
assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)
```