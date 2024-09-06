```python
from typing import List
def find_closest_elements(numbers: List[float]):
    # Initialize variables to compare
    smaller, closest = float('inf'), numbers[0]
    for num in numbers[1:]:
        if num < closest:
            smaller = num
            closest = num
    return smaller, closest
``` 
This function will take a list of numbers as input and will return a tuple of the two closest numbers in the list, along with the index of the smaller number.