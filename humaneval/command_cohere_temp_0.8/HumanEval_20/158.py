```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise ValueError("At least two numbers must be provided")
    elif len(numbers) == 2:
        return numbers[:2]
    else:
        middle = len(numbers) // 2
        left, right = numbers[middle - 1], numbers[middle]
        return find_closest_elements_(left, right, numbers)


def find_closest_elements_(left: float, right: float, numbers: List[float]):
    while numbers.index(left) > 0 and numbers[numbers.index(left) - 1] != left:
        left = numbers[numbers.index(left) - 1]
    while numbers.index(right) < len(numbers) - 1 and numbers[numbers.index(right) + 1] != right:
        right = numbers[numbers.index(right) + 1]
    if left == right:
        return left, left
    else:
        return left, right
```

The function `find_closest_elements` is a re-implementation of the `find_closest_elements_` function, making use of Python's efficient sorting algorithm, `sort()`, to sort the list of numbers. The `find_closest_elements_` function is then called with the first and last elements of the sorted list, avoiding an inefficient recursive loop and improving overall performance.