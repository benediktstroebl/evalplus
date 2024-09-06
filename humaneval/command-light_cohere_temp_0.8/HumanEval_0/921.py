Here is a self-contained Python script that solves the problem:
```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    # Use the Binary Indexing to compare the first two elements
    if numbers[0] <= numbers[1]:
        return True

    # Use the Binary Indexing to compare the last two elements
    if numbers[-1] <= numbers[-2]:
        return True

    return False


# Test the function
numbers = [1.0,2.0,3,0.0,0.8,3.0,5]
 if has_close_elements(numbers, 0.8) is False

print(has_close_elements(numbers, 0.8))  # This expected output True
```
The function `has_close_elements` takes in a list of numbers and a threshold. It uses binary indexing to compare the first two elements and then the last two elements in the list to check if any two elements are closer than the threshold. The output of the function will return True if any two elements are closer than the threshold and will return False if the condition is not met.