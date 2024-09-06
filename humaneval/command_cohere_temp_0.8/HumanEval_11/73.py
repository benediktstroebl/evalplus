```python
def string_xor(a, b):
    return str(int(a, 2) ^ int(b, 2))
```

This script defines a function `string_xor` that takes two strings `a` and `b` as inputs. It uses the `^` operator to perform binary XOR on the binary representations of these strings, converts the result back to a string using the `str` function, and returns the result. This operation is performed entirely within the function and does not rely on any external variables or interactions, making the function self-contained. 

To validate the functionality of the code, you can import the `unittest` module and create a test case, like this:
```python
import unittest

class TestStringXor(unittest.TestCase):
    def test_string_xor(self):
        self.assertEqual(string_xor('010', '110'), '100')
        self.assertEqual(string_xor('111', '001'), '110')
        self.assertEqual(string_xor('1000', '0001'), '1001')

if __name__ == '__main__':
    unittest.main()
```

This test suite will help ensure that the `string_xor` function is working correctly with different input combinations of binary strings.