```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Set the first and last elements as the candidates for the minimum distance
    min_dist = min(numbers[0] - numbers[-1])
    
    # Traverse the list to find the closest pair of elements
    for i in range(1, len(numbers)):
        current_dist = numbers[i] - numbers[i - 1]
        if current_dist < min_dist:
            min_dist = current_dist
            closest_element_index = i
    
    # Return the closest elements in order of decreasing value
    return tuple(numbers[closest_element_index - 1:]) + tuple(numbers[:closest_element_index])
```