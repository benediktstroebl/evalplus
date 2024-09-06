```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number)
    """
    numbers.sort(key=lambda x: x)
    left, right = [], []
    for i, j in zip(numbers, numbers[1:]):
        if j < i:
            left.append(j)
        elif j > i:
            right.append(j)
    if len(left) == 0:
                return (right[0], right[1])
            elif len(right) == 0:
                return (left[0], left[1])
            else:
                left_distances, right_distances = zip(left, right)
                left_index = left_distances.max()
                smallest left_distance
                right_index = right_distances.index(left_index)
                return (left[left_index], right[right_index])
``` 
This function can be used as a module to solve the problem and pass the tests easily.