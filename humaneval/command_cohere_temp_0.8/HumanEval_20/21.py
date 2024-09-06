```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    nums_sorted = sorted(numbers)
    diff = nums_sorted[1] - nums_sorted[0]
    for i in range(1, len(nums_sorted)):
        if i == 1 or nums_sorted[i] - nums_sorted[i-1] != diff:
            first, second = nums_sorted[0], nums_sorted[i]
            return first, second
    else:
        return nums_sorted[0], nums_sorted[-1]
```

The function sorts the list of numbers and then iterates through the sorted list, calculating the difference between each element and the previous one. If the difference is not the same as calculated previously, the algorithm assumes that the closest elements have been found. Otherwise, it finishes iteration and returns the first and last elements of the list, which, in case of a sorted list, guarantees the closest elements.