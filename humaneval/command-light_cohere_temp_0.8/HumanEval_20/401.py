```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    Selects and returns two numbers from the list that are closest to each other and returns them in order (smaller number, larger number).
    """
    # Sort the list of numbers
    sorted_numbers = sorted(numbers)
    
    # Get the first two elements of the sorted list
    first_two = sorted_numbers[:2]
    
    # Get the closest elements based on the definition of the distance
    closest_elements = (min(first_two), key=lambda x: x[0]), (max(first_two), key=lambda x: x[1])
    
    return closest_elements

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]

print(find_closest_elements(numbers)) )
```
This solution provides a function `find_closest_elements` that takes a list of numbers and returns a tuple containing the two closest elements. It uses the sorted() function to sort the input list of numbers and then selects the first two elements. It uses the key=lambda x: x[0] and x[1] arguments in the min() and max() functions to select the elements based on the desired definition of the distance.

This solution follows Python's type hints and follows the standard Python style guide. It is also uses a functional programming approach with a clear separation between the input parameter and the function logic, which improves the readability and maintainability of the code.