Here is a self-contained Python script that solves the problem you have described:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    Selects and returns two closest elements from the list and returns them in order of their difference.
    """
    return sorted(numbers, key=lambda x: (-x, 1), reverse=True))[:2][::-1]
```
This function takes a list of numbers as input and returns a tuple containing the two closest elements in the list, with the smaller value first. 
The function uses the sorted function to order the elements by their difference, and then takes the first two elements from the sorted list. 
The key argument to the sorted function is a lambda function that returns the difference between two elements. The reverse=True argument is used to ensure that the elements are ordered with increasing values. 
Finally, the function returns the first element of the tuple, which is the smaller of the two elements.