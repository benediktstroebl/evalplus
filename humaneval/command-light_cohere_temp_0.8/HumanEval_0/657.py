Here is a self-contained Python script with a function that checks whether any two elements in a list are closer to each other than a given threshold:

```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for i in numbers:
        for j in numbers:
            if abs(i - j) < threshold:
                return True
    return False
```

This function uses a nested loop to compare each element in the list to every other, and returns True if any pair is closer than the threshold. The function takes a list of numbers as input and a threshold as a parameter. The function returns a bool that indicates whether any two elements are closer than the threshold.