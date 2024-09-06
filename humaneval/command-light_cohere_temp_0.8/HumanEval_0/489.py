Here is a Python function that solves the problem:

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i]-numbers[j]) <= threshold:
                return True
    return False
```

This function takes a list of numbers and a threshold as input and returns a boolean indicating whether there are any two numbers in the list that are closer than the threshold. The function uses a nested loop to iterate through the list of numbers and checks if the absolute difference between each pair of numbers is less than or equal to the threshold. The function returns True if any of these conditions are met.

The function returns False by default, which means that it will return False if there are no pairs of numbers that are closer than the threshold.

This solution is a good starting point, but feel free to modify and improve it based on the specific requirements of the problem.