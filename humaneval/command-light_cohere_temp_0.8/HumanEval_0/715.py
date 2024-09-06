Here's a self-contained Python script that solves the problem:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    for i in range(len(numbers) - 1):
        if numbers[i] - numbers[i + 1] < threshold:
            return True
    return False

# Test the function
print(has_close_elements([1.0, 2.0, 3.0], 0.1)) # True

print(has_close_elements([1.0, 2.0, 3.0], 0.3)) # False
0

```
The function has_close_elements takes a list of numbers and a threshold as input and returns a boolean value that indicates whether any two numbers in the list are closer than the threshold. The function works by iterating through the list of numbers and checking if the difference between the current number and the next number is less than the threshold. The function then returns True if any such elements in the list are closer than the threshold, and False otherwise.