```python
def add(x: int, y: int):
    return x + y
```
```python
import pytest

def test_add():
    assert add(2, 3) == 5
    assert add(5, 7) == 12
```

This code defines a function called `add` that takes two integers as arguments (`x` and `y`) and returns their sum. This definition adheres to the function header outlined in the problem statement.

The tests are defined using pytest, a popular testing framework in Python. The `test_add` function specifically assesses the `add` function's correctness through two assertions. The first assertion verifies that the sum of 2 and 3 is equal to 5, whereas the second assertion confirms that 5 plus 7 equals 12. If both assertions pass, it signifies the `add` function's success in producing the anticipated results.