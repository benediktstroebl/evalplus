```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """ Selects and returns two elements that are the closest to each other from the list
    numbers and returns them in order of the distance. The closer one is the smaller number.
 <<return[0] = min(numbers[0],numbers[1])>>
return [numbers[0],numbers[1]]
```

The function `find_closest_elements` takes a list of numbers as input and returns a tuple containing the two closest elements from the list. It uses the Python's `min` function to compare the elements and returns the two elements in order of the distance.