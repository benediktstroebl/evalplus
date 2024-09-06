```python
def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    compare = None
    if type(a) == type(b):
        if isinstance(a, int) or isinstance(a, float):
            compare = a if a > b else b
        elif isinstance(a, str):
            la = len(a)
            lb = len(b)
            compare = a if la > lb else b
    return compare
```

This function compares two given variables with the if-based conditional statement. The function initially determines the types of both variables, ensuring they are the same. It then checks if the first variable is an integer or a float, sorting the values and returning the larger one. The function assumes the larger value is preferred if the values are strings, since it checks the length and returns the longer string. The 'compare' variable is returned once the larger value is found, or None if the values are equal. 

To make this script testable, it is recommended to define tests in a separate module and import them in a separate script to execute the tests, like this:
```python
import unittest
from compare_one import compare_one

class TestCompareOne(unittest.TestCase):
    def test_with_int(self):
        self.assertEqual(compare_one(1, 2), 1)
        self.assertEqual(compare_one(2, 1), 2)
        self.assertIsNone(compare_one(1, 1))

    def test_with_float(self):
        self.assertEqual(compare_one(1.5, 2.5), 2.5)
        self.assertEqual(compare_one(2.5, 1.5), 2.5)
        self.assertIsNone(compare_one(1.5, 1.5))

    def test_with_string(self):
        self.assertEqual(compare_one("1,5", "2,5"), "1,5")
        self.assertEqual(compare_one("2,5", "1,5"), "2,5")
        self.assertIsNone(compare_one("1,5", "1,5"))

if __name__ == '__main__':
    unittest.main()
```

This way, the script remains independent and reusable for other projects, and the tests are isolated and can be run together or separately.