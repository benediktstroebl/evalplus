```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ 
    Selects two numbers from the list that are closest to each other and returns them in order of larger number, smaller number
    """
    if len(numbers) < 2:
        return numbers[0], numbers[0]
    
    # Initialize the closest distance and closest elements.
    closest_distance, float('inf'), closest_elements = numbers[0]
    for number in numbers[1:]:
        current_distance = (number - closest_elements)**2
        closest_distance, new_elements = min(closest_distance, current_distance), (number, new_elements)
    return closest_distance, tuple(reversed(new_elements))

```
The function takes a list of numbers as an argument and returns a tuple containing the closest distance and the two elements. It uses the `min()` function to determine the smallest of the current closest distance and the current distance, and the two elements that form the new set of elements.