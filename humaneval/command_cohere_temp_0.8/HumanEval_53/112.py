```python
def add(x: int, y: int):
    return x + y
```
```python
import unittest

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_positive_numbers_second_case(self):
        self.assertEqual(add(5, 7), 12)

if __name__ == '__main__':
    unittest.main()
```
The code provides a Python script with a self-contained function `add` that solves the problem and passes the corresponding tests. 

The function `add` takes two integers as parameters and returns their sum. It includes type hints to indicate that the function expects integers.

The test suite, built using unittest, has two test methods that verify the behavior of the `add` function. `test_add_positive_numbers` checks if the function correctly adds two positive numbers, and `test_add_positive_numbers_second_case` verifies the addition of two different positive numbers. 

When executed, the `unittest.main()` call runs the test suite, ensuring that the `add` function complies with the expected behavior and the tests pass. 

This approach adheres to best practices in software development, including the use of testing frameworks and type hints, to deliver a robust and well-tested function.