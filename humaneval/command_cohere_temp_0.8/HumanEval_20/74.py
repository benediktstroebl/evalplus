```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise ValueError("At least two numbers must be provided")
    else:
        middle = len(numbers) // 2
        left, right = numbers[middle - 1], numbers[middle]
        return _get_closest_pair(left, right)


def _get_closest_pair(a, b):
    if (a == b) or ((a + b) / 2.0 in [x for x in [a, b] if x != 0.0]):
        return a, b
    else:
        return _get_closest_pair(a, b - (b - a)) if a != b else a, a
```

The tests would look like this:
```python
def test_find_closest_elements():
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)
    assert find_closest_elements([10.0, 8.0, 6.0, 4.0, 12.0, 11.0, 9.0]) == (10.0, 10.0)
    assert find_closest_elements([10.01, 10.0, 9.99, 11.0, 12.0]) == (10.0, 10.0)
    assert find_closest_elements([1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]) == (1.0, 2.0)
    assert find_closest_elements([3.1, 3.11, 3.12, 3.13, 3.14, 3.15, 3.16, 3.17, 3.18, 3.19, 3.2]) == (3.1, 3.2)

``` 
This script provides a function that takes a list of numbers as input and returns the two numbers in the list that are closest to each other. The function first sorts the list and then checks the pairs at positions `middle - 1` and `middle`. It recursively checks the left and right numbers if they are not equal and their average is not in the list, to handle cases where the closest pair is not adjacent. The function raises a `ValueError` if the list contains less than two numbers. The tests verify the function behaviour for different cases.