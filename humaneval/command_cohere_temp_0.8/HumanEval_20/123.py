```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise ValueError("At least two numbers must be provided")
    return numbers[0], numbers[-1]
```

Here's a short test case that can be used to verify the functionality:
```python
def test_find_closest_elements():
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)
    assert find_closest_elements([10.0, 20.0, 30.0, 40.0, 50.0, 12.0]) == (10.0, 12.0)
    assert find_closest_elements([10.0, 20.0, 30.0, 40.0, 50.0, 10.0]) == (10.0, 10.0)
    assert find_closest_elements([10.0, 20.0, 30.0, 40.0, 50.0, 22.0]) == (20.0, 22.0)
``` 

The `test_find_closest_elements` function provides a few different list scenarios to test the `find_closest_elements` function. It checks if the output is respectively `(2.0, 2.2)`, `(2.0, 2.0)`, `(10.0, 12.0)`, and `(10.0, 10.0)` for each of the scenarios.  The code expects these to be the closest numbers in each list, and the function passes the test if all assertions are `True`.  This can be executed directly in the Python environment to see the results `>> test_find_closest_elements()`.