Here's the code that can be used to check if any two elements in a list are closer than a given threshold:

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    # Return True if at least two elements in numbers list are closer than given threshold.
    for i in range(len(numbers) - 1):
        for j in range(i+1, len(numbers)):
            if numbers[i] - numbers[j] <= threshold:
                return True
    return False
```

This code uses a nested loop to iterate over the list of numbers and checks if any two consecutive elements are closer than the given threshold. It returns True if this condition is met, otherwise, it returns False.