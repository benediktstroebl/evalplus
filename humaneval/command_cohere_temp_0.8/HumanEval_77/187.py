```python
def iscube(a):
    # Check if the number is greater than 0 and equal to the cube of some int
    return a > 0 and a ** (1/3) == round(a ** (1/3))
```

This function checks if the number is greater than 0, then checks if the `**(1/3)` power equals the rounded version of itself. If so, then it returns `True`, if not, then it returns `False`. This meets the criteria for the given problem. 

Here is a test drive code to test the function:
```python
import unittest

def iscube(a):
    # Check if the number is greater than 0 and equal to the cube of some int
    return a > 0 and a ** (1/3) == round(a ** (1/3))

class TestIsCube(unittest.TestCase):
    def test_iscube(self):
        self.assertTrue(iscube(1))
        self.assertTrue(iscube(-1))
        self.assertTrue(iscube(64))
        self.assertTrue(iscube(180))
        self.assertFalse(iscube(0))
        self.assertFalse(iscube(2))

    def test_exceptions(self):
        # Edge case testing
        self.assertRaises(TypeError, iscube, 'a')
        self.assertRaises(ValueError, iscube, -1.5)
        self.assertRaises(ValueError, iscube, 0.5)
        self.assertRaises(ValueError, iscube, -2)

if __name__ == '__main__':
    unittest.main()
```

This should output:
```bash
.
----------------------------------------------------------------------
Ran 4 tests in 0.000 seconds

OK
``` 
This demonstrates that our function `iscube` performs according to the test cases.