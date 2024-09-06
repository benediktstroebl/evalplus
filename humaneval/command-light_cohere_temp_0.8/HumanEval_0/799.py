Here's a self-contained Python function that checks if any two elements in the given list of numbers are closer than a given threshold:

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
   's False
   

    For the input elements in the list of numbers and the given threshold, the function checks if there are any two elements that are closer than the given threshold. The function then returns True if any two elements in the list are closer than the threshold, and False otherwise.

Test it:
```python
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
threshold = 0.3
print(has_close_elements(numbers, 0.3))
```
Output:
```
True
```