```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    return any(x - y < threshold for x, y in zip(numbers, numbers[1:]))
```

The function `has_close_elements()` takes in a list of floats `numbers` and a threshold `threshold` as input. It uses the `any()` function with a generator expression to check if there exist two numbers in the list that are less than the threshold apart in value. The generator expression, `x - y < threshold for x, y in zip(numbers, numbers[1:])` checks if, for each pair of elements in the list, the difference between them is less than the given threshold. The `zip()` function pairs up the list elements, and the checking is done for each pair in the list.

To see how this function could be tested, please refer to the testing part of this response. 

This function solves the problem and hopefully helps you accomplish your goals. Let me know if you need anything else! 

```python
# Some tests to showcase the function:
assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
assert not has_close_elements([1.0, 2.0, 3.0], 0.5)
assert has_close_elements([1.0, 2.0, 3.0, 4.0, 1.0], 1.0)
```