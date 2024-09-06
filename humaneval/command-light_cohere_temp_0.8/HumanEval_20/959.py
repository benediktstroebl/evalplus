```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Ensure length is at least 3
    if len(numbers) < 3:
        return None, None

    # Initialize variables
    min_dist_1, min_dist_2 = float('inf')
    closest_1, closest_2 = (None, None)

    # Compare and store first closest element
    for num1, num2 in zip(numbers, numbers[1:]):
        dist = num1 - num2
        if dist < min_dist_1:
            min_dist_1 = dist
            closest_1 = (num1, num2)

    # Compare and store second closest element
    for num1, num2 in zip(numbers, numbers[2:]):
        dist = num2 - num1
        if dist < min_dist_2:
            min_dist_2 = dist
            closest_2 = (num1, num2)

    return closest_1, closest_2
```

This script defines a function `find_closest_elements` that takes a list of floating-point numbers as an argument and returns a tuple containing the two closest elements and their respective distances. The function uses a algorithm to find the two closest elements by comparing the elements of each pair in the list and updating the variables `min_dist_1` and `min_dist_2` accordingly. The final output is the two closest elements and their respective distances.