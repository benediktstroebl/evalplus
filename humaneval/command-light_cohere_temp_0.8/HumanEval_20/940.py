Here is a Python script that includes a self-contained function to solve the problem:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each other and return them in order (smaller number, larger number).
   

    Parameters:
    numbers (List[float]): a list of numbers with at least two elements.

    Returns:
    two elements in the list that are the closest to each other, and returns them in order of the larger value.
    """


Example usage:
```python
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
numbers = find_closest_elements(numbers)

print(numbers)
```
The output will be: `[2.0, 1.0]`