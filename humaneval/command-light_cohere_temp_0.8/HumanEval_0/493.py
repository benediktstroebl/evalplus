Here is a Python script that takes a list of numbers and a threshold as input, and returns `True` if any two consecutive numbers in the list are closer than the threshold:

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for i in numbers:
        for j in numbers[i+1:]:
            if abs(j - i) < threshold:
                return True
    return False
```
This function uses a nested loop to iterate through pairs of consecutive numbers in the list. It compares each number with the other and returns `True` if they are within the threshold. 

This function is a good starting point for solving the problem, and can be easily modified and customized to fit specific use cases.