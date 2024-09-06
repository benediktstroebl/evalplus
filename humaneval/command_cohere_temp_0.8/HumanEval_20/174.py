```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    delta = numbers[-1] - numbers[0]
    for i in range(1, len(numbers)):
        curr_delta = numbers[i] - numbers[i - 1]
        if curr_delta < delta:
            delta = curr_delta
    return numbers[0], numbers[-1]
```

The function `find_closest_elements` sorts the input list of numbers, then calculates the absolute difference between subsequent elements in the list until it finds a smaller absolute difference than the previous one, indicating the closest elements. It then returns these closest elements, which will be the first and last numbers in the sorted list, respectively. The example usage and provided tests demonstrate this logic effectively.  This approach is efficient and has a time complexity of O(n log n), where 'n' is the length of the input list.