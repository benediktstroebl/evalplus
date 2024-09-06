Here is a self-contained Python script that solves the problem:

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than given threshold
    """
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < threshold:
                return True
    return False
```

The script defines a function that compares all pairs of numbers in a given list, and returns true if any two numbers are closer than the given threshold. The function utilizes two nested loops, iterating over the list of numbers and comparing each pair of numbers.

The script is self-contained, and does not require any external functions or modules to be used. It can be used as a standalone function to solve the problem, and can be used in other scripts or programs as required.