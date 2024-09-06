Here's a self-contained Python script that provides a function to check if any two numbers in a given list are closer to each other than a given threshold:

```python
from typing import List
import math

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if math.sqrt(numbers[i]-numbers[j]) <= threshold:
                return True
    return False
```
This function compares each pair of numbers in the list using the absolute difference and if it finds that the difference is smaller than or equal to the given threshold, it returns True. 
You can use this function by passing a list of numbers and a threshold value to check if any elements in the list have the specified relationship.