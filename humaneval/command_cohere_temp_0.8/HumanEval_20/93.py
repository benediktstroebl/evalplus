```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise IndexError("List of numbers must contain at least two elements")
    else:
        middle = len(numbers) // 2
        left, right = numbers[middle - 1], numbers[middle]
        return (left, right) if left != right else (numbers[0], numbers[-1])
```

This function sorts the list of numbers and then identifies the closest elements, returning either the smallest and largest values or the only two distinct closest values, depending on the input list. This solution is efficient and easy to understand.