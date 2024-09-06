Here is a Python function that checks if any two elements in a list are closer than a given threshold:

```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) <= threshold:
                return True
    return False
```

This function uses a nested loop and the absolute value difference between any two numbers in the list to check if they are closer than the given threshold. The function returns `True` if any of the conditions are met, else it returns `False`.