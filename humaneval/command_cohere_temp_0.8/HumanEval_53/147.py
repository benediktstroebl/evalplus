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
In the above code, the `add()` function takes two arguments (`x` and `y`) and returns their sum. The `TestAddFunction` class contains two test methods that invoke the `add()` function with different input values and verify the output against the expected values using the `self.assertEqual()` method. When you run the script, the `unittest` module automatically executes the test methods and reports the results, highlighting any failures or successes.