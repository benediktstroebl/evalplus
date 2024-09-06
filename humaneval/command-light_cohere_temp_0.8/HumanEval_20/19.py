```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    numbers = [x for x in numbers if type(x) == float]
    if len(numbers) < 2:
        return numbers[0], numbers[0]
    
    if len(numbers) == 2:
        # Sort the numbers in ascending order
        numbers.sort()
        reverse= True
        # Select the two closest numbers and return them in order
        return numbers[0], numbers[1]
    
    # Error handling for lists with less than two elements
    raise ValueError("The list of numbers must have at least two elements.")
```
This function takes a list of numbers and returns a tuple of the two closest elements in the list, in ascending order. It raises an ValueError if the error occurs, such as the list having less than two elements.