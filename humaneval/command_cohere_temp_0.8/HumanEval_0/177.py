```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    return any(abs(x - y) < threshold for x, y in zip(numbers, numbers[1:]))
```

The function `has_close_elements()` takes in a list of numbers and a threshold as parameters. It uses the `any()` function with a lambda function to check for each pair of numbers in the list, subtracting one from the next one in the list (`x - y`) and checking if the absolute value of this difference is less than the threshold.

To test this script, you can create a list of numbers and a threshold and pass them as arguments, printing out the resulting boolean. Here is an example:
```python
numbers = [1.0, 2.8, 3.0, 4.0, 5.0, 2.0]
threshold = 0.3
print(has_close_elements(numbers, threshold))
```
This would print out `True` as the output, since the list contains the numbers `2.0` and `2.8`, which are closer than the threshold of `0.3`.

This way, the function solves the problem of checking if a given list of numbers contains elements that are closer to each other than a specific threshold.