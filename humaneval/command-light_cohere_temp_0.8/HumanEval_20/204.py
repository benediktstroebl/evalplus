Here's a self-contained Python script that solves the problem of finding the closest elements from a list of numbers:
```python
from typing import List, Tuple
def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers in ascending order
    numbers.sort(numbers)

    # Select the two numbers that are the closest to each other
    first_index = 0
    second_index = 0
    min_distance = float("inf")
    closest1 = None
    closest2 = None

    # Go through the list twice
    for _ in range(0, len(numbers) - 1):
        current_distance = numbers[first_index] - numbers[second_index]
        if current_distance < min_distance:
            min_distance = current_distance
            closest1 = numbers[first_index]
            closest2 = numbers[second_index]
        first_index += 1
        second_index += 1

    return closest1, closest2
```

This function takes a list of numbers as input and returns a tuple containing the two closest elements. The function first sorts the for ascending order and then finds the two closest elements. The closest elements are then returned in that order.