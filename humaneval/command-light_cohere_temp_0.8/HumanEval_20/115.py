Here's a self-contained Python script that solves the problem of finding the closest elements from a list of numbers:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Ensure length at least 2 for nearest neighbor calculation
    if len(numbers) < 2:
        return numbers, None
    
    # Calculate the distance between each pair of elements
    distances = [(x - y) ** 2 for x, y in zip(numbers)]
    
    # Sort the distances in ascending order
    sorted_distances = sorted(distances)
    
    # Find the two closest elements based on the sorted distances
    closest_elements = [num for num, _ in enumerate(sorted_distances) if sorted_distances[0] == sorted_distances[1]]
    
    return closest_elements[0], closest_elements[1]

```

This code defines a function called `find_closest_elements` that takes a list of floating-point numbers as an input and returns a tuple containing the two closest numbers in ascending order. The script ensures the numbers have at least two elements to work with, handles cases where the list has less than two elements, and calculates the distance between each pair of numbers using the Pythagorean distance formula. The distances are then sorted in ascending order, and the two closest numbers are selected based on the sorted distances. The function then returns the numbers that are the closest to each other.

This script can be used to solve the problem of finding the closest elements from a list of numbers in a self-contained manner.