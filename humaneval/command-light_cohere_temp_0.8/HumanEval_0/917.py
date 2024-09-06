Here's the self-contained Python script:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for i in range(len(numbers) - 1):
        if abs(numbers[i] - numbers[i + 1]) < threshold:
            return True
    return False

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
threshold = 0.3)
print(has_close_elements(numbers, 0.3)) # Output: True
```
This script defines a function called has_close_elements that takes a list of numbers and a threshold as input and returns a boolean indicating if any two numbers in the list are closer than the threshold. The function uses a loop to iterate through the list of numbers and compares each number with the next one, if the absolute difference between the two numbers is less than the threshold, then the function returns True. Otherwise, it returns False.

The example usage demonstrates the function by passing the numbers list and the threshold 0.3 to it, and prints the result, which is True, indicating that any two numbers in the list are closer than the threshold.