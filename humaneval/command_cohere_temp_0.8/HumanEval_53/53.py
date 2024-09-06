```python
def add(x: int, y: int):
    return x + y
```
```python
import unittest

class TestAddFunction(unittest.TestCase):
    def test_add_2_3(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_5_7(self):
        self.assertEqual(add(5, 7), 12)

if __name__ == '__main__':
    unittest.main()
```
The provided code includes the `add` function and a set of unit tests that verify its correctness. In the `add` function, two arguments, `x` and `y`, are added together using the `+` operator, and the result is returned.

The unit tests are defined using the `unittest` module. Specifically, the `TestAddFunction` class inherits from `unittest.TestCase`, enabling various test methods to conduct assertions. The `test_add_2_3` method verifies that the sum of 2 and 3 is equal to 5, and the `test_add_5_7` method verifies that the sum of 5 and 7 is equal to 12.

By using `unittest.main()` at the end of the script, all the defined test methods are executed when the script is run directly. This approach ensures that the `add` function behaves as expected and passes both tests, providing confidence in its correctness.