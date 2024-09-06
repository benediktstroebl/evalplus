Here is a Python script that checks whether any two elements in a list are closer than a given threshold:

```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) <= threshold:
                return True
    return False
```
This function iterates through a list of numbers, checking if any two consecutive elements are closer than a given threshold. It returns True if any of these conditions are met, and False otherwise.