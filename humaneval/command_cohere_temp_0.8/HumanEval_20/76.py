```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise IndexError("List of numbers must have a minimum of two elements")
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
    return left, right
```

The function `find_closest_elements` leverages Python's `sorted` function to sort the list of numbers and retrieve the two closest numbers on the fly, without the need for nested loops, and thus optimizes the algorithm. It selects the middle two elements if the list is of odd length, or if the list has an even length, it recursively selects the closest of the first two elements and the last two elements of the sorted list.  A potential improvement to the function could be utilizing a heap or priority queue, which would permit the saving of the nearest valued pairs and their further retrieval.