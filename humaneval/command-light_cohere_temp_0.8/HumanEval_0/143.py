Here's a self-contained Python function that checks if any two elements in a list are closer than a given threshold:

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    the given threshold.
    """
    return any of the list has two elements with a distance less than threshold
    """
    return any(map(lambda x, y: x != y and abs(x - y) < threshold, numbers))
```
This function uses the map function with a lambda function to iterate through the list of numbers. The lambda function checks if the two elements are equal and if the absolute difference between them is less than the threshold.

The function returns True if any such condition is met, indicating that there are two numbers in the list that are closer than the threshold. 

It returns False otherwise.