Here's a self-contained Python script that defines a function called `has_close_elements` that checks if any two numbers in a given list of numbers are closer than a given threshold:

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] - numbers[j] <= threshold:
                return True
    return False
```

This function takes a list of numbers and a threshold as input and returns a boolean indicating whether any two numbers in the list are closer than the threshold. 

This function uses a nested loop to iterate through the list of numbers and checks if the difference between any two consecutive numbers is less than or equal to the given threshold.