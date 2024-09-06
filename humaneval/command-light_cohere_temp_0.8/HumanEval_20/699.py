```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    Selects and returns two elements from the list that are the closest to each other and returns them in order (smaller number, larger number).

    Parameters:
        numbers: List[float] - A list of numbers of length at least two.

    Returns:
        Tuple[float, float] - A tuple containing the two closest elements in the list in order of their values.

Example usage:
>>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0])
(2.0, 3.0)

```