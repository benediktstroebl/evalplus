Here is a Python script that has a self-contained function that checks if any two numbers in a given list are closer to each other than a given threshold:

```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for i in numbers:
        for j in numbers:
            if abs(i - j) < threshold:
                return True
    return False
```

This function has a List[float] and a float threshold as input and returns a bool that is True if any two numbers in the list are closer to each other than the threshold. It uses nested loops to compare each pair of numbers and returns True if any comparison is True.