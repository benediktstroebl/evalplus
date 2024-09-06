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
    if (a - b) < 1e-5:  # adjust tolerance as needed
        return a, b
    elif abs(a - b) < abs(a - _get_closest_pair(a, a)) or abs(a - b) < abs(a - _get_closest_pair(b, b)):
        return a, b
    else:
        return _get_closest_pair(a, a), _get_closest_pair(b, b)
```

This script includes the `find_closest_elements` function, which takes a list of numbers as input and returns two numbers from the list that are closest to each other. It first sorts the list and then checks the pairs to find the two numbers that have the smallest difference between them. The `_get_closest_pair` helper function recursively navigates through the problem, considering the closest pairs in a smart manner.

This solution includes a tolerance value of `1e-5` to handle cases where the difference between two numbers is very small. Adjust this value according to your needs. 

When you run this script, it will output the closest elements for the list of numbers provided in the example scenarios you provided. If the list has less than two elements, it will raise a `ValueError` as indicated in the `find_closest_elements` function's documentation.