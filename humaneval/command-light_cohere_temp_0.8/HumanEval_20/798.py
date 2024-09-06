Here is a self-contained Python script that solves the problem you have provided:

```python
from typing import List
from typing import Tuple
def find_closest_elements(numbers: List[float]):
    """ Selects and returns two closest elements from a supplied list of numbers and returns them in order (smaller number, larger number).
    numbers: List[float]
    closest1, closest2 = float('inf'), float('-inf')
    for num in numbers:
        if num < closest1:
            closest1, closest2 = num, closest1
            break
    return closest1, closest2
```

This script defines a function **find_closest_elements** that takes a list of numbers as an input and returns a tuple of the two closest numbers. The function uses a specific typing features from the Python **typing** module and also uses a loop to find the two closest numbers.