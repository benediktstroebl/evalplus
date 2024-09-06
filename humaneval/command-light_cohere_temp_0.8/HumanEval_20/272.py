```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ 
    Returns a tuple of the two closest elements in the list. 
    - From provided list, and returns them in order of (smaller number, larger number).
    """
    # Initialize the two closest elements and the current elements in the list
    closest_pair = (float('inf'), float('-inf'))
    for num, index in enumerate(numbers):
        # Calculate the distance between the current element and the closest element in the pair
        current_distance = (num - closest_pair[0]) * (num - closest_pair[0])
        
        # If the current distance is less than the current closest pair, update the closest pair
        if current_distance < closest_pair[1]:
            closest_pair = (num, current_distance)
        
        # If the current element is closer to the closest element in the pair, update the current closest pair
        elif current_distance < closest_pair[0]:
            closest_pair = (num, current_distance)
            
    return closest_pair

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
 expected output: 
```

This code defines a function `find_closest_elements` that takes a list of numbers as an argument and returns a tuple containing the two closest elements. The function uses a simple Euclidean distance formula to calculate the distance between each number in the list and the current closest pair. It then iterates through each element in the list and updates the current closest pair if the current element is closer to the current closest pair. If the current element is already closer to the current closest pair, it checks if the current closest pair should be updated by comparing the current distance with the distance of the closest pair.