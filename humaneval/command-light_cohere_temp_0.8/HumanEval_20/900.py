Here is a self-contained Python script that solves the problem of finding the two closest elements from a list of numbers:
```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers in ascending order
    sorted_numbers = sorted(numbers)
    # Initialize two lists to store the closest elements
    closest_elements = [sorted_numbers[0]]
    distance_to_next = [float("inf")]

    # Iterate through the sorted list and update the closest element and distance to the next number
    for i in range(1, len(sorted_numbers)):
        current_element = sorted_numbers[i]
        next_element = sorted_numbers[i - 1]

        # Calculate the distance between the current and next elements
        distance = abs(current_element - next_element)

        # If the distance is less than the current distance to the next number
        if distance < distance_to_next[1]:
            closest_elements.append(next_element)
            distance_to_next[1] = distance

    # Return the closest elements and their distances
    return closest_elements, distance_to_next
```

This function takes a list of numbers as input and returns a tuple of the two closest elements in the list and their corresponding distances. The function works by first sorting the list of numbers and then iterating through the sorted list to find the two closest elements. The function uses the efficient algorithms like sorting and calculating the distance between elements to quickly find the closest elements.