```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    return any(abs(a - b) < threshold for a, b in zip(numbers, numbers[1:]))
```

The function `has_close_elements()` takes in a list of floats `numbers` and a threshold value `threshold` and checks if any two numbers in the list are closer to each other than the threshold. It uses a list comprehension with a generator expression, also known as a 'Zip trick', to iterate through all pairs of adjacent elements in the list `numbers`, and compares each pair to verify if their absolute difference is less than the `threshold`. The `any()` function then checks if any of these comparisons are `True`, and returns `True` if at least one pair of elements has a difference less than the threshold, and `False` otherwise.

To see it in action, you can call the function with the example test cases provided in the problem statement, like this:
```python
print(has_close_elements([1.0, 2.0, 3.0], 0.5))
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))
```

The output will be:
```
False
True
```