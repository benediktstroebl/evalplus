```python
def add(x: int, y: int):
    """
    Add two numbers x and y
    """
    return x + y
```
```python
import unittest

class TestAddFunction(unittest.TestCase):
    def test_add_two_numbers_with_2(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_five_and_seven(self):
        self.assertEqual(add(5, 7), 12)

if __name__ == '__main__':
    unittest.main()
```
The code provides a Python script with a function `add` that solves the problem; it adds two numbers `x` and `y`. The script also includes a test class `TestAddFunction` that verifies the function's correctness through two distinct tests, ensuring that the code passes the added numbers' summation. 
The function is straightforward, with a clear docstring describing its purpose, and the test case uses the `unittest` module to ensure that the function behaves as expected.