```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Initialize the first and second closest elements to None
    first, second = None, None
    for num in numbers:
        if first is None or num < first:
            first = num
        elif second is None or num < second:
            second = num
    if first is not None and second is not None:
        return (first, second)
    return None

# Unit tests
test_data = [1.0, 2.0, 3.0, 4.0, 2]
test_closest_elements(test_data) is (2.0, 1.0))
test_data = [1.0, 2.0, 3.0, 5.0, 2]
test_closest_elements(test_data) is (3.0, 2.0))
test_data = [1.0, 2.0, 2.0, 3.0, 5.0]
test_closest_elements(test_data) is (2.0, 3.0))
test_data = [1.0, 2.0, 4.0, 5.0, 2]
test_closest_elements(test_data) is (5.0, 2.0))
test_data = [1.0, 2.0, 3.0, 4.0, 5.0, 2]
test_closest_elements(test_data) is (4.0, 3.0))
test_data = [1.0, 2.0, 3.0, 4.0, 5.0, 2]
test_closest_elements(test_data) is (1.0, 5.0)]
```