Here is a Python script that implements the function `find_closest_elements(numbers)`, which accepts a list of floating-point numbers as input and returns a tuple containing the two closest numbers along with their respective distances.

This function employs the method of sorting the input list to determine the two closest numbers and then reverses the order of these numbers to return them in the correct order. The function also returns the results as a tuple, ensuring that the return values are the correct ones.

Here's the code:
```python
from typing import List, Tuple
import math

def find_closest_elements(numbers: List[float]) ->
    # Sort the input list of numbers
    sorted_numbers = sorted(numbers)
    
    # Initialize variables
    smallest_num = sorted_numbers[0]
    second_num = sorted_numbers[1]
    distances = [(smallest_num, math.0)]
    
    # Loop through to find the two closest numbers
    for i in range(1, len(sorted_numbers)):
        current_num = sorted_numbers[i]
        
        # Calculate the distance between the current number and the two already found numbers
        current_distance = math.sqrt((current_num -a -distance(smallest_num, current_num))**2 + (current_num - second_num)**2)
        
        # Check if the current number is closer than the two already found numbers
        if current_distance < distances[0]:
            distances[0] = current_distance
        elif current_distance < distances[1]:
            distances[1] = current_distance
        else:
            # If the current number is not closer, it is not a closer number
            distances.append((current_num, math.0))
    
    # Return thetime is to return the two closest numbers
    return distances
```

This function uses the `distance` function to calculate the Euclidean distance between two numbers. The function then compares these distances to determine the two closest numbers.