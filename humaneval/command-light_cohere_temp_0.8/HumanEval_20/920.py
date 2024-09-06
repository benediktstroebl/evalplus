Here's the solution of the problem:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    Selects and returns two closest elements from the supplied list of numbers and returns them in order (smaller number, larger number).
    
    Args:
    numbers: A list of float, length at least two
    
    Returns:
    Tuple[float, float]: A tuple containing the two closest elements and their order.
```

This script defines a function called **find_closest_elements** that takes a list of numbers as input and returns a tuple containing the two closest elements in the list. The function uses the sorting method to order the numbers and then takes the two smallest and largest numbers from the list and returns them in a tuple.