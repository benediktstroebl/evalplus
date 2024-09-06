```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the numbers
    numbers.sort(numbers)
    # Take the two closest elements
    closest = (numbers[0] if numbers[0] < numbers[-1] else numbers[-1])
    return (numbers[0], closest)

# Test
def test_find_closest_elements(test_numbers):
    expected = (2.0, 1.2)
   
    test_numbers = test_numbers.sort()
    double_tuple(sorted(test_numbers)))
    actual = find_closest_elements(test_numbers)
    assert actual == expected
```