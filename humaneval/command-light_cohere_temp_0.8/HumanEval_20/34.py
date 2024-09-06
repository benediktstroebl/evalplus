```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # initialise the first and second closest elements
    first, second = (numbers[0] , numbers[1])
    # check if the length of the list is at least 2
    if len(numbers) <= 2:
        return (numbers[0], numbers[1])
    # sort the list of numbers
    numbers.sort()
    return (numbers[0], numbers[1])
```
The function takes a list of numbers as an argument and returns a tuple containing the two closest elements in the list. It does this by initializing the first and second closest elements from the list. It also checks if the0 length of the list is at least 2, and if it is, it returns the elements (numbers[0] , numbers[1]) as the closest elements, as this is the only possible solution.

It then sorts the list of numbers and returns the first and second elements in the list as the closest elements.