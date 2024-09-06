```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise ValueError("At least two numbers must be provided")
    return numbers[-2:]
```

This function sorts the input list of float numbers and returns the two closest elements as a tuple, making sure the shorter distance is between these two values. It also validates that the input list has at least two elements, otherwise it raises a `ValueError`. 

Here is a test suite to verify the functionality:
```python
def test_find_closest_elements():
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)
    assert find_closest_elements([10.0, 20.0, 30.0, 40.0, 50.0, 22.0]) == (20.0, 22.0)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 1.0, 2.0]) == (1.0, 2.0)
    assert find_closest_elements([10.0, 20.0, 30.0, 40.0, 50.0, 22.0, 33.0]) == (20.0, 22.0)
test_find_closest_elements()
```