Here's a self-contained Python script with a function that solves the problem of determining if any two numbers in a given list are closer than a given threshold:

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if math.sqrt(numbers[i] - numbers[j]) <= threshold:
                return True
    return False
```

This script defines a function that takes in a list of numbers and a threshold as input. The function then loops through each element in the list and checks if any two elements are within the threshold by using the `math.sqrt()` function to calculate the sqrt of the square of each number.

Finally, the function returns `True` if any two numbers in the list are within the threshold, and `False` otherwise.