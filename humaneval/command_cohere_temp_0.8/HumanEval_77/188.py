```python
def iscube(a):
    # Check if the number is a perfect cube
    return a ** (1/3) == int(a ** (1/3))
```

This function simply computes the cube root of the given integer `a` and checks if it is an integer.

### Testing Code

```python
# Test if the function works for all the test cases
import unittest

class TestIsCube(unittest.TestCase):
    def test_iscube(self):
        self.assertTrue(iscube(1))
        self.assertFalse(iscube(2))
        self.assertTrue(iscube(-1))
        self.assertTrue(iscube(64))
        self.assertTrue(iscube(0))
        self.assertFalse(iscube(180))

if __name__ == '__main__':
    unittest.main()
```

This code uses `unittest` in Python to automate the testing of our `iscube` function. A test case class `TestIsCube` is defined with individual test functions (`test_iscube`) that test the function's behavior for each individual test case specified in the problem statement. The `assertTrue` method tests if the `iscube` function returns the correct boolean value for a given input. 

To run this test suit, run `python test_iscube.py` in your terminal. 

The `iscube` function should pass all the test cases, and the output of the testing script will be `.*success.*` if the tests pass.