Here is a self-contained Python script that solves the problem you have described:

```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """
    from typing import List
    from math import sqrt

    numbers = [x for x in numbers if len(numbers) == 2]
    numbers.sort()
   0, numbers[::1] = numbers[1] - numbers[0]
    numbers[0] = 0
    min_distance = float('inf')
    closest_index = 0
    for i in range(1, len(numbers)):
        current_distance = (numbers[i] - numbers[0])**2
        current_index = i
        if current_distance < min_distance:
            min_distance = current_distance
            closest_index = current_index

    closest_value, closest_index = numbers[closest_index]
    return closest_value, closest_index
```
The function `find_closest_elements` takes a list of numbers as input and returns a tuple containing the two closest elements in the list, along with their index in the original list.