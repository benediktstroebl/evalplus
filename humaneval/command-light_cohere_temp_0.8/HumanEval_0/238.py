```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # iterate through list and compare numbers
    for i in range(len(numbers) - 1):
        if numbers[i] - numbers[i+1] < threshold:
            return False
    return True

# tests
numbers = [1.0, 2.0, 3.0, 0.0, 4.0, 5.0]
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.0]
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 0.0, 0.0, 3]
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 0.0, 4.0]
numbers = [1.0, 2.0, 3.0, 4]
numbers = [1.0, 2.0, 3.0, 5]
numbers = [1.0, 2.0, 0.0]])
numbers = [1.0, 2.0, 3.0, 4]
numbers = [1.0, 2.0, 0]
numbers = [1.0, 2.0, 3]
numbers = [1.0, 2.0, 0.0, 3]
numbers = [1.0, 2.0, 0]
numbers = [1.0, 2.0, 3]
numbers = [1.0, 2.0, 0.0, 0]
numbers = [1.0, 2.0, 0]
numbers = [1.0, 2.0, 0]
numbers = [1.0, 2.0, 0]
numbers = [1.0, 2.0, 0]
numbers = [1.0, 2.0, 0]
numbers = [1.0, 2.0, 0]
numbers = [1.0, 2.0, 0]
numbers = [1.0, 3.0, 0]
numbers = [1.0, 3.0, 0]
numbers = [1.0, 3.0, 0]
numbers = [1.0, 4.0, 0]
numbers = [1.0, 5.0, 0]
numbers = [1.0, 6.0, 0]
numbers = [1.0, 7.0, 0]
numbers = [1.0, 8.0, 0]
numbers = [1.0, 9.0, 0]
numbers = [1.0, 10.0, 0]
numbers = [1.0, 11.0, 0]
numbers = [1.0, 12.0, 0]
numbers = [1.0, 13.0, 0]
numbers = []
```