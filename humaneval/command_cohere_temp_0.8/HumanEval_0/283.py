Here's a Python script that contains a function called has_close_elements, which takes a list of numbers and a threshold as input and returns a boolean indicating whether any two numbers in the list are closer to each other than the threshold. The function works correctly and passes the provided tests. The code is formatted as a markdown code block:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    """
    numbers.sort()
    for i in range(1, len(numbers)):
        if numbers[i] - numbers[i - 1] < threshold:
            return True
    return False

# Tests
assert not has_close_elements([1.0, 2.0, 3.0], 0.5)
assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
```

The function first sorts the input list of numbers. Then, it iterates through the list, and checks if the difference between each element and the next element is smaller than the given threshold. If any of these differences is smaller, it indicates that there are closely spaced elements, and the function returns True. If none of the differences are smaller, it returns False, indicating that no closely spaced elements were found.