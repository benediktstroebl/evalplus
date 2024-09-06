```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] - numbers[j] < threshold:
                return False
    return True
```
This function checks if in a given list of numbers, any two numbers are closer to each other than the given threshold. The function loops through the and checks if the two elements are within the threshold.