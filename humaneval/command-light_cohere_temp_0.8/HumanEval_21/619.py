```python
from typing import List
def rescale_to_unit(numbers: List[float]) -> List[float]:
    # Initialize the new numbers list with the same values
    new_numbers = [num / 100 for num in numbers]
    return new_numbers
``` 
The function rescale_to_unit takes a list of numbers and returns a new list with the same values, but rescaled to the unit 0 to 1. 
This is a self-contained function, meaning that it does not rely on any other functions or variables from outside its scope and can be fully tested by passing the function with a list of numbers.