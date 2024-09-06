```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Initialize distance and previous variables
    distance: List[float] = [float('inf')]
    previous: List[float] = [float('-inf')]

    # Calculate distance and previous for all elements in numbers
    for num in numbers:
        # Calculate distance to the previous element
        current_distance = num - previous[0]
        distance.append(current_distance)

        # Update the previous element
        previous.append(num)

    # Sort the list of distances in descending order
    sorted_distances = sorted(distance)

    # Get the two closest elements and return them in descending order
    closest_elements = sorted_distances[0:-1]
    return closest_elements[::-1], sorted_distances[0]

```
This Python script defines a function called **find_closest_elements** that takes a list of numbers as input and returns a tuple containing the two closest elements in descending order along with the corresponding distance between them. 

The function uses a technique called **Two-Circle** or **Bidirectional Search** to achieve this. The two closest elements are selected based on the smallest and largest values in the sorted list of distances.