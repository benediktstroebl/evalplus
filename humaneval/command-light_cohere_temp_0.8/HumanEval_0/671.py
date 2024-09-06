Here is a Python script that defines a function called has_close_elements that checks if any two elements in a list are closer than a given threshold. It accepts a list of numbers as input and a threshold as a parameter, and returns a boolean value indicating whether there are any pairs of elements that are closer than the threshold.

Here is the Python code:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    for i in range(len(numbers) - 1):
        if numbers[i] + numbers[i + 1] < threshold:
            return True
    return False

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
threshold = 0.3)
print(has_close_elements(numbers, 0.3)) # True
```
This script defines a function that checks if any two elements in a list are closer than a given threshold. The function returns a boolean value, which is True if any two elements in the list are closer than the threshold, and False otherwise.

It uses a loop to iterate through the list of numbers and checks if the sum of the two elements at the current index is less than the given threshold. The function returns True if any pair of elements are closer than the threshold, and False otherwise.

The example usage at the bottom demonstrates how to call the function with a list of numbers and a threshold, and prints the result.