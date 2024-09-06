```python
from typing import List
def find_closest_elements(numbers: List[float]):
    # Declare variables to store the two closest numbers and their corresponding distances
    closest1 = float('inf')
    closest2 = float('-inf')
    distance1 = float('inf')
    distance2 = float('-inf')
    # Initialize the first element of the tuple
    result = (closest1, distance1)
    # Loop through the list of numbers
    for num in numbers:
        # Calculate the distance to the current number
        distance = abs(num - closest1)
        # Update the closest number if a smaller distance is found
        if distance < distance1:
            closest1 = num
            distance1 = distance
        # Otherwise, update the second closest number and its distance
        elif distance < distance2:
            closest2 = num
            distance2 = distance
        # After the loop, update the result tuple
        else:
            result = (closest2, distance2)
    return result
```
The function "find_closest_elements" accepts a list of numbers as an input and returns a tuple with the two closest numbers and their corresponding distances. The function uses the precise distance calculation and employs a loop to identify the two closest values. The result tuple is updated as each new number is evaluated.