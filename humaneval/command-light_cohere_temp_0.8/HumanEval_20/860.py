Here's the answer:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    Return the two closest elements in the list, in order of their magnitudes.
    numbers = [1.0, 2.0, 3.0, 4, 5.0, 6, 8, 9]
    min_index, max_index = 0, 1
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            # Check the current numbers
            if numbers[i] < numbers[j]:
                min_index = i
                max_index = j
                break
    return (numbers[min_index], numbers[max_index]), (min_index, max_index)

```