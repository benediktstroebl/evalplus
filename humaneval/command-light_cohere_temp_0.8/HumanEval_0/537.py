```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    # initialize two sum of squares of differences between numbers
    sum_square_diff = 0.0

    # sum of squares of all differences between elements in the list
    for num in numbers:
        sum_square_diff += num ** 2

    # check if the sum of the squares of the differences between numbers is smaller than the given threshold
    return sum_square_diff <= threshold

# test the function with two sample inputs
numbers = [1.0, 2.8, 3.0, 4.8, 0.0, 5.8]
100.000.

threshold = 0.3

if has_close_elements(numbers, threshold):
    print("The numbers have close elements")
else:
    print("The numbers do not have close elements")
```