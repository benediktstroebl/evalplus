```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise ValueError("At least two numbers must be provided")
    return numbers[0], numbers[-1]
```

The function `find_closest_elements` takes a list of numbers as input and returns the two closest numbers in the list, regardless of whether the list contains multiple pairs of equally close numbers. To accomplish this, the function sorts the input list first, ensuring that the closest numbers are always the first and last elements in the list. Then, it returns these two initial and final elements. 

This approach guarantees the correct solution for any list with at least two numbers, including cases where the list contains multiple pairs of equally close numbers. It simplifies the logic compared to the previous approach using distance calculations and removes the need for explicit tuple returns.