```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # check if list has two adjacent numbers
    if len(numbers) < 2:
        return False

    # check for numbers that are closer than the threshold
    for i in range(1, len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] - numbers[j] <= threshold:
                return True

    return False

# Test
if has_close_elements([1.0, 2.0, 3.0, 0.0], 0.5):
   0)

else:
    print("Not all numbers have closer elements")
```