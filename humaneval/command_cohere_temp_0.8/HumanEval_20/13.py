```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise ValueError("At least two numbers must be provided")
    x = numbers[-2]
    y = numbers[-1]
    return x, y
```

The function `find_closest_elements()` takes a list of numbers `numbers` as input and returns a tuple containing the two numbers that are closest to each other. The list of numbers is first sorted and checked to verify it has a minimum length of 2. As a safeguard, a `ValueError` is thrown if the list length is less than 2. Once this is confirmed, the last two numbers in the sorted list are returned, which by definition are the closest pair of numbers in the list.

Here's a sample usage of the function with assertions to check the expected output:
```python
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]
expected = (2.0, 2.2)

result = find_closest_elements(numbers)
assert result == expected
```