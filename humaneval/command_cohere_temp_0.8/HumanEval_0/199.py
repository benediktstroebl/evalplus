Here's a Python script that contains a function called has_close_elements, which takes a list of numbers and a threshold as input and returns a boolean indicating whether any two numbers in the list are closer to each other than the threshold. The function works correctly and passes the given tests. The code is formatted as a markdown code block:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    """
    return any(abs(a - b) < threshold for a in numbers for b in numbers if a != b)

# Tests
assert not has_close_elements([1.0, 2.0, 3.0], 0.5)
assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
```

The function uses a generator expression with nested loops to compare each number in the list to every other number in the list, ignoring the same number. The any function then checks if there are any comparisons that yield a difference smaller than the given threshold. The function returns True if there are such comparisons, and False otherwise.  The tests assert the function's correctness for the given use-cases.  This code defines the function and the tests in a self-contained manner, making it easy to reuse and test the functionality.  This approach follows best practices in software development, as it is self-contained, tested, and has a meaningful docstring that describes the function's purpose and usage.  If needed, you can copy and paste this code block into a Python file to use it directly in your projects.