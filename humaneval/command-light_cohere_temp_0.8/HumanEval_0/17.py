Here is a self-contained Python script that solves the problem you provided:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] - numbers[j] < threshold:
                return True
    return False

# Test
has_close_elements([1.0, 2.0, 3.0, 0.0, 4.0, 5.0, 2.0], 0.3)
 has_close_elements([1.0, 2.0, 3.0, 4.0], 0.4)
Return: False

This script defines a function `has_close_elements` that takes in a list of numbers and a threshold as parameters. It then iterates over the numbers in reverse order and checks if the difference between the two numbers is less than the given threshold. It returns `True` if any two numbers are closer than the threshold, indicating that the list has at least one pair of consecutive close elements.