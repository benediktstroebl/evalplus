```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Initialize variables to store the two closest numbers and their relationship.
    closest1 = float("INF")
    second_closest = float("-INF")
    closest_index = 0
    for index in range(len(numbers)):
        # Calculate the difference between the current number and the two closest numbers.
        distance = numbers[index] - closest1 - second_closest
        if distance < 0:
            closest1 = distance
            closest2 = distance
            second_closest = distance
            closest_index = index
    else:
        pass
    # Return the two closest numbers and their relationship
    return closest1, closest2, closest_index
```
This function takes a list of numbers as input and returns a tuple of the two closest numbers and their index, where the numbers are returned in descending order. 

The function works by iterating through the list of numbers and calculating the difference between each number and the two closest numbers. It then uses this specific logic to select the two closest numbers based on their distance and updates the variables to store the values of the two closest numbers.