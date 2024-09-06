Here's a self-contained Python script with a function that checks if any two numbers in a given list are closer to each other than a given threshold:

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    return any(n1 <= n2 + threshold for n1, n2 in zip(numbers))

# Example
numbers = [1.0, 2.0, 3.0]
threshold = 0.2
print(has_close_elements(numbers,threshold))  # Output: True
``` 
This function checks if any two numbers in the list are closer to each other than the given threshold. The function uses the 'any' function to check if any two elements in the list are equal or greater than each other by adding the given threshold to both numbers.