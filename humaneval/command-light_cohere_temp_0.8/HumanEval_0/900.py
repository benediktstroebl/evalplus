Here is a Python script that takes a list of numbers and a threshold as input and returns True if there are any two numbers in the list that are closer to each other than the threshold:

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold

    if any(n1 <= threshold and n2 <= threshold for n1, n2 in numbers, n1 in numbers) and n2 in numbers):
        return True
    else:
        return False
```

This function uses the condition that checks if any of the numbers in the list are smaller than the threshold and then checks if the number is still in the list. It returns True if it meets the required conditions.