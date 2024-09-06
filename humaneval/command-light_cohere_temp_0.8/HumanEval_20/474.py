```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Compare two numbers
    x, y = min(numbers[0] , numbers[1]), - max(numbers[0] , numbers[1])
    # Return the smaller number first
    return (x, y)

# Test case
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]
return find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0])
return (2.0, 4.0)
```