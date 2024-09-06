```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    from typing import List
    l1, l2 = min(numbers), max(numbers)
    return l1, l2

# Test the function with a list of numbers
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
#

print(find_closest_elements(numbers))
```

This function is designed to find the two closest elements in a list of numbers and return them in descending order. The function uses the min and max functions from the typing module to select the two closest elements.