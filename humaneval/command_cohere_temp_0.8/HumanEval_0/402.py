```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    return any(x - y < threshold for x, y in zip(numbers, numbers[1:]))
```

The function `has_close_elements()` takes in a list of numbers and a threshold as inputs, and returns a boolean indicating whether any two numbers in the list are closer to each other than the threshold. 

To do this, the function uses a generator expression, `any(x - y < threshold for x, y in zip(numbers, numbers[1:]))`. This iterates through pairs of numbers in the list using the `zip` function, and checks if the difference between each pair is less than the given threshold. If any of these differences are less than the threshold, the `any` function will return `True`, indicating that the list contains closely spaced numbers. 

This approach ensures that the function is efficient for large lists, as it only needs to check each number pair once, and it elegantly handles the querying of numeric proximity in varying lists.