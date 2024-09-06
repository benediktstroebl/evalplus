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
The provided code includes the `add` function and a set of unit tests that validate its behavior. The `add` function accepts two integers as parameters and returns their sum. The test suite, comprised of the `test_add_positive_numbers` and `test_add_positive_numbers_second_case` test cases, verifies that the function correctly computes the sum of 2 and 3 and 5 and 7, respectively. When the script is executed, the `unittest.main()` function runs all the defined tests. In this instance, since no assertion fails, the output reflects that all test cases were successfully executed.