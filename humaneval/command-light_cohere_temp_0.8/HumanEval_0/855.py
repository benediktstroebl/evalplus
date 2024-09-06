Here is a self-contained Python script that defines a function has_close_elements that checks if any two numbers in a given list are closer than a given threshold:

```python
from typing import List
import math

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    return any( abs(n1 - n2) < threshold for n1, n2 in numbers) )
    """
    for n1, n2 in zip(numbers, numbers):
        if abs(n1 - n2) < threshold:
            return True
    return False
```
This code defines a function that checks if any two numbers in a list are closer than a given threshold. It uses the for loop to iterate over the list of numbers and checks if the absolute difference between any two numbers is less than the given threshold.