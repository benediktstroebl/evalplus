```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    Selects and returns two elements from the list that are the closest to each other and returns them in order (smaller number, larger number).
    numbers = [1.0, 2.0, 3.0, 4, 5, 6]
    elements = sorted(numbers, key=lambda x: (x, -x) )
    closest1 = elements[0]
    closest2 = elements[1]
    return closest1, closest2
```
This function takes a list of numbers and returns a tuple containing the two elements in the list that are the closest to each other. The function uses the algorithm that selects the two elements with the smallest and largest values and returns them in order. This algorithm works by sorting the list of numbers based on the values of each element and selecting the two elements with the smallest and largest values.