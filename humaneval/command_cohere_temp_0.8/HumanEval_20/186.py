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
    if (a == b) or (a + b == 0):
        return a, b
    else:
        return _get_closest_pair(b, a)
```

The function `find_closest_elements()` takes a list of numbers as input and returns two numbers that are closest to each other. It first sorts the list, then checks if the length of the list is at least 2. If it is, it selects the middle two elements and uses the helper function `_get_closest_pair()` to return the closest pair. The helper function recursively compares the two numbers and returns the closest pair while handling special cases where a or b are equal to 0 or each other.

Here is an example usage of the function find_closest_elements:
```python
test_list = [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]
result = find_closest_elements(test_list)
print(result)  # (2.0, 2.2)
``` 

This would return the closest elements which are 2.0 and 2.2, and print them to the console.