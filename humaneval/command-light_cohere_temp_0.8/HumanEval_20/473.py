```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ Selects and returns two elements in the list that are the closest to each other, and returns them in order (smaller number, larger number).

    Parameters:
        numbers: List[float] - A list of numbers

    Returns:
        Tuple[float, float] - A tuple containing two closest numbers in order of the above.
```

def test_find_closest_elements():
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]
   
    # Find the closest elements and return them in order.

test_find_closest_elements()