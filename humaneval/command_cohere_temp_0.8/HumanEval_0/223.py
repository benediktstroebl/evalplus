Here's a Python script that contains a function called has_close_elements, which takes a list of numbers and a threshold as input and returns a boolean indicating whether any two numbers in the list are closer to each other than the threshold. The function works correctly and passes the provided tests. The code is formatted as a markdown code block:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    """
    numbers.sort()
    for i in range(len(numbers) - 1):
        if numbers[i + 1] - numbers[i] < threshold:
            return True
    return False

# Tests
assert not has_close_elements([1.0, 2.0, 3.0], 0.5)
assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
```

This script includes a function called has_close_elements, which takes two inputs: a list of numbers and a threshold. The function sorts the numbers and then iterates through the list, checking if the difference between each element and the next one is less than the given threshold. If any of these differences is less than the threshold, the function returns True, indicating that there are two numbers close to each other in the list. Otherwise, it returns False.