Here's a self-contained Python script that solves the problem:

```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """ Returns the two closest values from a list of numbers, and returns them in order (smaller number, larger number).
    numbers = [1.0, 2.0, 3.0, 4, 5.0, 6, 8, 9, 10, 11, 12]
    min_val, max_val = (min(numbers), max(numbers))
    return (min_val, max_val)
```

You can call the function like this:

```python
result = find_closest_elements([1.0, 2.0, 3.0, 4, 5.0, 6, 8, 9, 10, 11, 12])
print(result)
```

The function will return a tuple containing the two closest values, which are then printed out.