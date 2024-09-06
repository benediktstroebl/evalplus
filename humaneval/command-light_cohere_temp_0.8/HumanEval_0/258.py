```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    return any(abs(x - y) <= threshold for x, y in zip(numbers))
```
This function checks if any two numbers in the list are closer than the threshold. It returns a boolean value that is True if there are any such pairs, and False otherwise.

You can use this function to test its functionality with a sample list of numbers and a given threshold.

Here is an example test:
```python
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
threshold = 0.2)
result = has_close_elements(numbers, 0.2)
print(result)
```
This code will print True because the numbers in the list have a closer pair than the given threshold.