Certainly, here's the Python script that includes the self-contained function `strlen()`:

```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test cases
assertEqual(strlen(''),     zero_length())
assertEqual(strlen('abc') ,  3)
assertEqual(strlen('')) ,  zero_length()

# Test suite
if __name__ == '__main__':
    import unittest
    unittest.result = TestRunner(verbosity=3)
    unittest.result.unittest()
```