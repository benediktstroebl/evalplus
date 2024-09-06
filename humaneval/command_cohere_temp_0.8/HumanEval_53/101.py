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
The code provides a Python script with a self-contained function `add` that solves the problem; it takes two integers `x` and `y` as arguments and returns their sum. The script also includes a corresponding test suite utilizing the `unittest` module with two test cases that verify the correctness of the `add` function against specified inputs. When executed, the test suite will automatically run all the tests and report any failures or errors, ensuring the expected behavior of the `add` function is met.