```python
from typing import List
def find_closest_elements(numbers: List[float]):
    # Sort the numbers in ascending order
    sorted_numbers = sorted(numbers)
    # Take the first two elements in the sorted list
    first_two = sorted_numbers[:2]
    # Return the smaller number first
    return first_two[0], sorted_numbers[0]
```
This code defines a function `find_closest_elements` that takes a list of numbers as input and returns a tuple with the two closest numbers in the list. This is then selecting the two closest elements, the function first sorts the input list of numbers, then takes the first two elements in the sorted list. Then, it returns the largest number and the original number.