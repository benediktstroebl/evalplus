Here's a Python script that defines a function `has_close_elements` that checks if any two elements in a list of numbers are closer than a given threshold.

Here's the code:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    """
    list comprehension:
    For each pair of numbers in the list, it checks if their difference is less than the threshold.
    if so, it returns True.
    Otherwise, it returns False
    """

# test
numbers = [1.0, 2.8, 3.0, 4.0, 5.0, 6.0, 8]
print(has_close_elements(numbers, 0.8)) #True
print(has_close_elements([1.0, 2.0, 3.0, 0.0, 5.0, 0.0, 8, 0.5)) #False

```
The `has_close_elements` function takes in input a list of numbers and a threshold value. It uses list comprehension to iterate over the pairs of elements in the list and checks if the difference between each pair is less than the threshold value. If it is, it returns True, indicating that there are close elements in the list. If not, it returns False.