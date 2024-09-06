```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    return any(x - y < threshold for x, y in zip(numbers, numbers[1:]))
```

The function `has_close_elements()` takes in a list of floats `numbers` and a threshold `threshold` and returns a boolean indicating whether any two elements in the list are closer to each other than the threshold. It uses a generator expression `any(x - y < threshold for x, y in zip(numbers, numbers[1:]))` which iterates through pairs of elements in the list using the `zip()` function, and checks if the difference between each pair is less than the threshold. The `any()` function then determines if any of these differences are less than the threshold and returns `True` if so, and `False` otherwise. 

To see it in action, you can call the function with the example inputs provided in the problem statement, like so:
```python
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # Should print False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # Should print True
``` 

This will help verify the function's correctness against the provided cases. 

I hope this solution suits your needs; please let me know if you have any further questions or if you'd like assistance with any other coding problems or topics!