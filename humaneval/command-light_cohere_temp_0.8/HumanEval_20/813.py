Here's a self-contained Python script that solves the problem:

```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """
    Sort the list of numbers and return two closest values and their order
    """
    numbers.sort(key=lambda x: x)
    # Return the first two closest numbers in sorted list
    return (numbers[0], numbers[1])
```

You can use this function by passing a list of numbers as an argument. For example:

```python
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]

print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2]))
```
This will output the two closest elements in the list, which are 1.0 and 5.0, and the order (1.0, 2.0> in descending order.