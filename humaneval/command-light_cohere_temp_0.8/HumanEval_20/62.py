```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """
    Selects and returns two numbers from the input list that are the closest to each other and returns them in order (smaller number, larger number).
    """
    # Initialize a tuple to store the two closest elements
    closest = (float('inf'), float('-inf'))
    
    # Initialize a counter to keep track of the number of elements in the list
    counter = 0
    
    # Iterate through the list and update the closest tuple and the counter
    for num in numbers:
        distance = num - closest[0]
        if distance < closest[1]:
            closest = (num, distance)
            counter += 1
    
    # Return the closest tuple
    return closest

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print_closest_elements(numbers)
```

This function takes a list of numbers as input and returns a tuple with the two closest elements. The function initializes the closest tuple with the maximum and minimum possible float values. It then iterates through the value of each element in the list and updates the closest tuple if a smaller distance is found. Finally, the function returns the closest tuple, which contains the two closest elements in the list.