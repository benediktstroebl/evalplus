Here is a Python script that defines a self-contained function that performs the XOR operation on strings:
```python
import stringixor as ixor
import unittest

class StringXORTestCase( ixor.StringXOR_ ):
class StringXORTestCase(unittest.TestCase):
    def test_string_xor(self):
        self.assertEqual("010", "110")
        self.assertEqual("100", "010")
        self.assertEqual("0000", "0011")
        self.assertEqual("1111", "1110")
        self.assertEqual("1010", "1001")

        result = ixor.StringXOR("010", "110")
        self.assertEqual(result, "100")

        result = ixor.StringXOR("00", "0")
        self.assertEqual(result, "0")

        result = ixor.StringXOR("0000", "11")
        self.assertEqual(result, "1111")

        result = ixor.StringXOR("1111", "10")
        self.assertEqual(result, "1010")

        result = ixor.StringXOR("1010", "1001")
        self.assertEqual(result, "1010")

if __name__ == '__main__':
    unittest.main()
```

This script contains a function `StringXORTestCase` that extends the `unittest` framework and defines a number of test cases for the `string_xor` function. The function then runs `unittest.main()` to execute the run the tests.