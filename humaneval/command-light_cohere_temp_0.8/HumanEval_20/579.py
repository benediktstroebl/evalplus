```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # initialize distance and previous variables
    distances: List[float] = []
    previous: List[float] = []

    # calculate and store the distance between each pair of elements in the list
    for i in range(len(numbers)):
        current_distance = numbers[i] - numbers[(i - 1) % len(numbers)]
        distances.append(current_distance)
        previous.append(current_distance)

    # sort the list of distances in ascending order
    sorted_distances = sorted(distances)

    # sort the list of previous values in descending order
    sorted_previous = sorted(previous)

    # take the first element of the sorted list of distances and the last element of the sorted list of previous values
    first_element, second_element = sorted_distances[0], sorted_previous[-1]
    return (first_element, second_element)
```
This function takes a list of numbers and returns a tuple of the two closest elements in the list. The function works by first calculating the distance between each pair of elements in the list and then sorting the list of distances in ascending order. Then, the function sorts the list of previous values in descending order and finally returns the first element of the sorted list of distances and the last element of the sorted list of previous values.