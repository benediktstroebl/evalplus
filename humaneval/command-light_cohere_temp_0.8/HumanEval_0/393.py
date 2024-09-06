```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < threshold:
                return True
    return False

# Test
test_data = [1.0, 2.0, 3.0, 0.0, 0.8, 5.0, 2.0, 4.0]
return has_close_elements(test_data, 0.8)  # Returns True
```
This script defines a function called `has_close_elements` that checks whether any two numbers in a given list are closer than each other than a given threshold. The function iterates over the two lists from the start of each list and compares each element in the first list with each element in the second list. It then returns True if any of these comparisons return True. The function is tested with a test data that contains a list of numbers and a threshold value.