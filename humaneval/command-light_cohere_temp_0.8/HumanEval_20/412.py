```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """
    Return the two closest elements in the list, in order of their larger values.
    """
    smallest_num, largest_num = (numbers[0], numbers[-1])
    for i in range(1, len(numbers)):
        current_num, current_largest = numbers[i], numbers[-i-1]
        if current_num < smallest_num:
            smallest_num, largest_num = current_num, current_largest
        elif current_num > largest_num:
            smallest_num, largest_num = current_num, current_largest
    return smallest_num, largest_num
```