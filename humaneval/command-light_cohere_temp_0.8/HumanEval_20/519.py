```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    Selects two numbers from the list that are closest to each other. Returns the two values in order (smaller number, larger number)
    """
    comparison = sorted(numbers, key=lambda a: (1.0, -a))
    first, second = comparison[0], comparison[1]
    return comparison[0], comparison[1]

# Example
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
result = (2.0, 5.0)
print("The closest numbers are ")' + format(result))
```