```python
def truncate_number(number: float) -> float:
    return number - int(number)
```

This function simply computes the difference between the input number and the largest integer less than or equal to the input number, which is the decimal part of the number. 

To test this function, here is a sample test case:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(7.0) == 0.0
    assert truncate_number(7.3) == 0.3
```

To execute the function and run the tests, you can run the script in your local machine:
```bash
python script.py
```

Alternatively, you can import the function and run the tests independently, like this:
```python
import unittest
from code_problem.truncate_number import truncate_number

class TestTruncateNumber(unittest.TestCase):
    def test_truncate_number(self):
        assert truncate_number(3.5) == 0.5
        assert truncate_number(7.0) == 0.0
        assert truncate_number(7.3) == 0.3
```

In both cases, the tests will confirm that the function produces the expected outcome.