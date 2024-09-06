```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers
    numbers.sort(numbers)
    # Return two closest numbers and return them in order (smaller number, larger number)
    return (numbers[0], numbers[1])

# Test the function with a sample input
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print_closest_elements(numbers)
``` 
This Python script defines a function named `find_closest_elements` that aims to find and return pairs of the closest numbers from a given list of numbers. The function takes a list of floating-point numbers as input and utilizes the `sort()` method to sort the list in ascending order.

The function then creates a tuple containing the first and second elements of the sorted list, which represent the two closest numbers. 

Finally, the function is tested with a sample input list `[1.0, 2.0, 3.0, 4.0, 5.0] and the printout results output, which is the tuple `(numbers[0], numbers[1])`, indicating that the first and second elements of the sorted list are the closest numbers and are returned in that order.