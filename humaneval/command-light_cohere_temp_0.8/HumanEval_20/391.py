Here's the solution to the problem:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    numbers.sort()
    sorted(numbers, key=lambda x: x)
    closest = Tuple(numbers[:-index])
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i-1]:
            closest = Tuple(numbers[:i]) + Tuple(numbers[i:])
    return min(closest[0], closest[1]), closest
```

This function takes a list of numbers as input and returns a tuple containing the two closest elements in the list. The function first sorts the necessary list of numbers and then uses the sorted list to find the closest elements. The function then uses a list of tuples to find the closest elements in the list.

The function also passes the test of being self-contained, as it does not require any external dependencies or function calls to solve the problem.