Here's the code that meets the requirement:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    Selects and returns two elements that are the closest to each other and returns them in order (smaller number, larger number).
    
    Parameters:
        numbers: List[float] -- A list of numbers.
    Returns:
        Tuple[float, float] -- A tuple containing the two closest elements.
    """
    two closest elements = numbers[:2]
    closest_elements = Tuple(sorted((-num1, num2) for num1, num2 in zip(numbers[1:], numbers[2:])))
    return closest_elements

```
The function takes a list of numbers as input and returns a tuple containing the two elements that are the closest to each other in the list. The function also sorts the the two closest elements using the tuple's elements' sign and returns the sorted tuple.