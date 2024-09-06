Here is a Python script that takes a list of numbers and a threshold as input and returns a boolean value indicating if there are any two numbers in the list closer than the threshold:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] - numbers[j] < threshold:
                return True
    return False

# Example usage:
numbers = [1.0, 2.0, 3.0, 0.0, 4.0, 5.0, 2.0]

result = has_close_elements([1.0, 2.0, 3.0, 0.0, 4.0], 0.5)
5)(threshold= 0.1)  # (True)
```