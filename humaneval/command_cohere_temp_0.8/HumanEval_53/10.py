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

This code defines a function called `add` that takes two integers as arguments (`x` and `y`) and returns their sum. This definition is followed by a block of test code using the `pytest` framework, which checks whether the `add` function behaves as expected when given specific inputs. 

The `test_add` function verifies that the `add` function returns the correct results for two different sets of input values: (`2`, `3`) and (`5`, `7`). 

To execute this code, you can either copy it into a Python file (e.g., `add.py`) or use an IDE or Python environment that supports editing and running individual scripts. After executing the file, the `pytest` framework will run the automated tests, ensuring the `add` function's correctness against the provided expected output.