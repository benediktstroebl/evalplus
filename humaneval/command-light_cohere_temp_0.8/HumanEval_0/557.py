Here is a self-contained Python script that solves the problem of checking if any two numbers in a list are closer than a given threshold:
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

This function takes two parameters: `numbers`, which is the list of numbers that we want to check, and `threshold`, which is the threshold that we want to compare the numbers in the list to.

The function loops over the range of indices of the `numbers` list, and for each pair of adjacent elements, it checks if the difference between those two numbers is less than or equal to the `threshold`. If the condition is met, the function returns `True`. Otherwise, it returns `False`.

This function is a self-contained solution that can be used as-is in markdown code blocks to solve the problem.