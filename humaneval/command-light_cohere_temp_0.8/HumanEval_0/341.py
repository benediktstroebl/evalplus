Here's the solution for the problem:

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    the threshold.
    """
    return any of the pair in numbers such that their Euclidean distance is less than or equal to the threshold.
 could be added to a list [i,j] such that i <= j <= len(numbers)
    """
    return any(n1 <= threshold and n2 <= threshold for numbers[i], numbers[j] for i,j in numbers)
```