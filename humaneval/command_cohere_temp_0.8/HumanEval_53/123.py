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
The provided code includes the `add` function and a set of unit tests that verify its correctness. In the `add` function, two arguments, `x` and `y`, are added together using the `+` operator, and the result is returned. 

The unit tests are defined using the `unittest` module. The `TestAddFunction` class inherits from `unittest.TestCase`, enabling various assertion methods provided by the base class. 

Within this class, two test methods are defined: `test_add_positive_numbers` and `test_add_positive_numbers_second_case`. These methods exercise the `add` function with different inputs and validate whether the output matches the expected result using the `assertEqual` method. 

When the script is executed, the `unittest.main()` function is called, which discovers and runs all test methods defined in the module. 

Overall, this code provides a self-contained solution to the problem and demonstrates the usage of unit tests to ensure the correctness of the `add` function.