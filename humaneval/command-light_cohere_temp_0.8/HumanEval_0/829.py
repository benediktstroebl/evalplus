Here is a self-contained Python script with a function that checks if any two numbers in a given list are closer to each other than a given threshold:

```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    return any(x <= y for x, y in zip(numbers, numbers[1:])) and numbers == numbers[0:][::-1]
for x, y in zip(numbers, numbers[1:]):
    if x <= y:
        return True
    else:
        return False

# Test
numbers = [1.0, 2.0, 3.0, 0.2, 0.8, 4.0, 5.0, 2.0, 0.2, 0.8, 3]
has_close_elements([1.0, 2.8], 0.001)
print("The result of has_close_elements is %True") 
```
This script defines a function `has_close_elements` that takes in a list of numbers and a threshold as input. The function returns `True` if any two numbers in the list are closer than each other than the threshold. The function uses the `zip` function to iterate over the list, and checks if the current element is less than or equal to the next element. The function also checks if the list is reversed and contains the same elements. The function returns `False` otherwise.

The test section shows an example of how to use the `has_close_elements` function with a given list of numbers and a threshold. The output should be printed to show the result of the function.