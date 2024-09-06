```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    return any(abs(x - y) <= threshold for x, y in numbers)
    return True
```
The function checks if any two numbers in the list are closer than the threshold. It uses the boolean condition and the any() function, which returns True if any element in the list matches the condition.

The time complexity of this code is O(n), where n is the length of the input list, as it uses the any() function, which iterates over all elements in the list once.

This function can be used to check if any two numbers in a list are closer than a given threshold, and it can be used to solve the problem in a markdown code block.