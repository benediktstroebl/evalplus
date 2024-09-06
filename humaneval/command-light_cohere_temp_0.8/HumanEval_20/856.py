Here's a Python script that includes a self-contained function that solves the problem of finding the closest elements in a list of numbers:

```python
from typing import List
from typing import Tuple

def find_closest_elements(numbers: List[float]):
    # Return the two closest elements in the list
    closest1 = float('inf')
    closest2 = float('-inf')
    for num in numbers:
        if num < closest1:
            closest1 = num
        elif num < closest2:
            closest2 = num
    else:
        return closest1, closest2
    return closest1, closest2
```

The function will return the two closest elements in the list and return them in order (smaller number, larger number).