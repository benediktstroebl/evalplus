```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers
    numbers.sort(numbers)
    
    # Get the two closest numbers
    x1 = min(numbers)
    x2 = max(numbers)
    
    # Return the two numbers and their order
    return (x2, x1)

# Example
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print_closest_elements(numbers)
``` 
This Python function, find_closest_elements, takes a list of numbers and finds the two closest elements to each other, then returns them in order (smaller number, larger number). The function uses the min and max functions to find the minimum and maximum numbers, respectively. The two closest numbers are then returned as a tuple.