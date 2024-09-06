Here is a self-contained Python function that checks for the presence of closely-adjacent elements in a list of numbers, using a given threshold:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    return any(x <= threshold for x in numbers[1:]) and any(y >= threshold for y in numbers[:-len(numbers)-1])
```

The above function checks if there are any two elements in the list that are closer than the given threshold. If the condition is satisfied, then it returns True, else it returns False.