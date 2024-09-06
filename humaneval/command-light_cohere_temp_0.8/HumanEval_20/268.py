```python
from typing import List
def find_closest_elements(numbers: List[float]):
    """ Selects and returns two of the numbers in numbers that are the closest to each other, and returns them in order (smaller number, larger number).
    """
    closest1 = float('inf')
    closest2 = float('-inf')
    for n1, n2 in zip(numbers, numbers[1:]):
        if n1 < closest and n2 < closest2:
            closest = n1
            closest2 = n2
    return closest, closest2
```
This code implements the function `find_closest_elements`, which takes a list of numbers as input and aims to find the closest pair of elements in the list. It does this using a `zipping` of the list to create a new list of elements in pairs, and iterates through this new list to compare each pair to the closest pair. The function returns the` closest` and `closest2` to hold the respective values.