```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    if len(numbers) < 2:
        raise ValueError("Need at least 2 elements to find the closest pair")
    else:
        min_distance = float("inf")
        min_element, max_element = None, None
        for i in range(0, len(numbers)):
            current_distance = numbers[i] - numbers[(i + 1) % len(numbers)]
            if current_distance < min_distance:
                min_distance = current_distance
                min_element, max_element = (i + 1) % len(numbers), numbers[i])
        return min_element, max_element
```
The function takes a list of numbers and returns a tuple of the two closest elements and their respective distances. The function handles the values in the list to maintain the order of the elements in the returned tuple.

Please note that this function does not handle the case where the list contains only one number. If you have a useful input, we can enhance the function to handle such cases appropriately.