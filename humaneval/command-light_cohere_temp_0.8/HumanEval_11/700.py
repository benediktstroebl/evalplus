```python
import stringcase
import unittest

def string_xor(a: str, b: str) -> str:
    return "".join(chr(c ^ b.get(c)) for c in a)

class TestStringXor(unittest.TestCase.TestCase):
   
    class common_string_pairs()
    for test_case in test_cases:
        result = string_xor(test_case[0], test_case[1])
        unittest.TestCase.assertEqual(result) is a same_case

common_string_pairs = ["010", "110", "0011", "1010", "0110", "001122"]
test_cases = [test_case for test_case in common_string_pairs]

if __name__ == "__main__":
    unittest.run(TestStringXor)()
```
This Python code defines a function `string_xor` that performs the XOR operation of two strings, treating each character as a binary digit and taking the XOR of the bits. The function then implements a test suite using the unittest framework. The test suite contains a common string pairs that can be used to test the function.

Finally, the `unittest.run` command is the function and verify its correctness.