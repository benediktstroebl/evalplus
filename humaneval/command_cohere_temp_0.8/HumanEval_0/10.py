```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    return any(abs(x - y) < threshold for x, y in zip(numbers, numbers[1:]))
```

The function `has_close_elements` takes in a list of numbers and a threshold as input, and returns a boolean indicating whether any two numbers in the list are closer to each other than the threshold. The function examines each pair of numbers in the list using the `zip` function, calculating the absolute difference between each pair of numbers. It then uses the `any` function to check if any of these differences are less than the given threshold. If any of the differences are less than the threshold, the function returns `True`, indicating that there are close elements in the list; otherwise, it returns `False`. 

To see it in action, you can call the function with the example inputs provided in the problem statement, like this:
```python
print(has_close_elements([1.0, 2.0, 3.0], 0.5))
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))
```

This will yield the desired output, namely `False` for the first case and `True` for the second one.