Here is a Python script that solves the problem:

```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """
    Returns the two closest elements from the list, in order of their larger values.
    """
    n = len(numbers)
    if n < 2:
        return (numbers[0], numbers[0])
    else:
        first, second = zip(numbers[:n // 2], numbers[n // 2:])
        return (first[0], second[1])

# Driver code
numbers = [1.0, 2.0, 3.0, 4.0, 2]

result = find_closest_elements(numbers)

print(result)
```