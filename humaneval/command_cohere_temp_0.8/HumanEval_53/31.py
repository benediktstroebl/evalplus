```python
def add(x: int, y: int):
    return x + y
```
```python
import unittest

class TestAddFunction(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(add(2, 3), 5)

    def test_larger_values(self):
        self.assertEqual(add(5, 7), 12)

if __name__ == '__main__':
    unittest.main()
```

The code provides a Python script with a self-contained function `add` that performs addition on two provided integers. It includes a corresponding test suite using the `unittest` module with two test cases: one for verifying the addition of 2 and 3, and another for verifying the addition of 5 and 7. The `unittest.main()` function is used to discover and run the test cases when the script is executed directly. In this way, the code presents a complete solution to the problem with fully automated tests.  This safeguards against unintended changes in the future.