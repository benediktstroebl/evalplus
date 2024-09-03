Here is a Python script that contains a self-contained function that solves the problem:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # sort the list ascending and check for the threshold
    if numbers:
        numbers.sort(reverse = True)
        for i in range(len(numbers)):
            if numbers[i] - threshold < numbers[0]:
                return True
        for i in range(len(numbers)):
            if numbers[i] - numbers[i - 1] > threshold:
                return True
        return False

# test
nums = [1.0, 2.0, 3.0, 0.0, 0.0, 5.0, 2.0]
return has_close_elements(nums, 0.0)  # should return True
```

Note that this function solves the problem by checking if any two consecutive elements are closer than a given threshold, and returns True if this is the case.