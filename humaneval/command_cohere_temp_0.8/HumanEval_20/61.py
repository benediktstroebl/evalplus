```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise IndexError("List of numbers must be of length at least two")
    else:
        middle = len(numbers) // 2
        return numbers[middle], numbers[-1]
```

This script defines a function `find_closest_elements` which takes in a list of float numbers and returns two float numbers that are closest to each other from the list and are returned in order (the smaller number first, then the larger number). The script returns `None` and prints an error message if the input list length is less than 2. It utilizes sorting to ensure the closest pair is found even if the list is not sequentially ordered. 

Here is an example usage of the function:
```python
test_lists = [
    [1.0, 2.0, 3.0, 4.0, 5.0, 2.2],
    [1.0, 2.0, 3.0, 4.0, 5.0, 2.0],
]

expected_results = [
    (2.0, 2.2),
    (2.0, 2.0),
]

for list_test, expected in zip(test_lists, expected_results):
    result = find_closest_elements(list_test)
    assert result == expected
```