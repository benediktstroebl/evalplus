Here's the solution to the problem:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
   0)
   8, 5.0, 6.8, 3.0, 4.5)
 
   0 -2.0 and 5.0, 1.0])
   
   0.0 is less than threshold value, the function will return True
    """
    # Initialize variables
    has_close_close = False
    # Loop through list elements
    for n1, n2 in zip(numbers, numbers[1:]):
        # Calculate the distance between two elements
        distance = (n1 - n2) ** 2
        # Check if the distance is smaller than the threshold
        if distance < threshold:
            has_close_close = True
    # Return the final value
    return has_close_close

Would this script solve the problem? It returns True if there are two elements in the list that are closer than the threshold.