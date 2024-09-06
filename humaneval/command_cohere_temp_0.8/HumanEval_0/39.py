```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    return any(abs(a - b) < threshold for a, b in zip(numbers, numbers[1:]))
```

The function `has_close_elements` takes in a list of numbers and a threshold as inputs, and returns a boolean indicating whether any two numbers in the list are closer to each other than the threshold. The function checks if the absolute difference between any two consecutive elements in the list is smaller than the threshold. 

To test this function, we can create a test harness that checks the function's behavior against specific input [1.0, 2.0, 3.0] and expected output False, as indicated in the problem statement. Here is a corresponding test:
```python
def test_has_close_elements():
    assert not has_close_elements([1.0, 2.0, 3.0], 0.5)
```

[1] Solutions without any dependencies such as `zip`, and `any` are also possible, depending on the version of Python being used.