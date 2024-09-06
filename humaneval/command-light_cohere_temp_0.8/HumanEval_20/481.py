Here is the provided Python script that solves the problem of finding the closest elements in a list of numbers:
```python
from typing import List, Tuple
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ Finds the two closest elements in the list and returns them in order of their difference """
    if len(numbers) < 2:
        raise ValueError("List of numbers must contain at least two elements")
    # Sort the list of numbers in ascending order
    numbers.sort(key=lambda x: x, - x)
    # Initialize the first and second elements in the list as the first and last elements, respectively
    first, second = numbers[0], numbers[-1]
    # Initialize two variables to store the closest elements and their respective distances
    closest_element_1, closest_element_2, distance = (first, float('inf')), (second, float('inf'))
    # Find the minimum distance between the two elements and update the variables
    for i in range(len(numbers) - 2):
        current_first, current_second = numbers[i], numbers[i + 1]
        current_distance = (current_first - current_second) ** 2 + (current_second - current_first) ** 2
        if current_distance < distance[0]:
            closest_element_1, closest_element_2, distance = (current_first, current_distance), (current_second, current_distance)
    # Return the closest elements and their respective distances
    return closest_element_1, closest_element_2, distance
```
This function takes a list of numbers and returns a tuple containing the two closest elements in the list and their respective distances. The function first sorts the both the smallest number and the largest number. If the list of numbers contains less than two elements, the function raises a ValueError exception.