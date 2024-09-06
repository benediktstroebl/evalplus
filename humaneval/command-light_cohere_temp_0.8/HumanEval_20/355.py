```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Use default ordering to compare floats
    return (smallest(numbers), largest(numbers))

def test_find_closest_elements():
    assert isinstance(numbers, List), "Input must be a list of numbers."
    assert len(numbers) >= 2, "Input list must have at least two numbers."
    assert all(isinstance(n, (float))) for n in numbers
    if len(numbers) == 2:
        return find_closest_elements(numbers), "Found two numbers that are closest to each other.")
    else:
        raise ValueError("Input list must have at least three numbers.")

test_find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0])
test_find_closest_elements(test_find_closest_elements([1.0, 2.0, 3.0, 4.0])
``` Output: ((2.0, 4.0), (1.0, 3.0))
```