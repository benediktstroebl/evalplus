```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # initializing variables
    min_val = float("inf")
    max_val = float("-inf")
    closest_pair = None

    # Looping to find the closest elements
    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            # Finding the current minimum and maximum values
            current_min = numbers[i]
            current_max = numbers[j]

            # Updating variables based on the new minimum and maximum values
            min_val = min(current_min, min_val)
            max_val = max(current_max, max_val)

            # Checking if the current pair is the closest pair
            if current_min < numbers[i] and current_max > numbers[j]:
                closest_pair = (current_min, current_max)
                break

    # returning the closest pair of numbers
    return closest_pair

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]


result = find_closest_elements(numbers)
```