```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    # Sort the list in ascending order
    sorted_numbers = sorted(numbers)
    # Initialize two variables with the first two elements in the sorted list
    a, b = sorted_numbers[0], sorted_numbers[1]
    # Loop until the two variables a and b have different values
    while a != b:
        # Calculate the absolute difference between the current numbers a and b
        diff = abs(a - b)
        # Check if the difference is less than the given threshold
        if diff <= threshold:
            return True
        a, b = a + 1, b + 1
    return False
```
This Python script defines a function called `has_close_elements` that checks whether any two numbers in a given list are closer to each other than a given threshold. The function works by first sorting the list of numbers and then comparing the first two elements to find a pair of numbers that satisfy the condition. The script then loops through the pair until a pair that doesn't satisfy the condition is found.