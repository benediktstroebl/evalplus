Here's a self-contained Python function that checks if any two numbers in a list are closer than a given threshold:

```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 6.1.0, 0.8, 6.0, 8.0, 9.0, 0.9, 10.0, 11.0, 10, 0.1, 12]
    numbers
    for this function, you have to pass in a list of numbers and a threshold value. The function will then check if there are any two numbers in the list that are closer than the threshold value. If there are any such closer numbers, the function will return True. If not, the function will return False.