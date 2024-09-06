```python
def iscube(a):
    # Check if the number is greater than 0 and equals to a power of 3
    return a > 0 and ((a**(int(math.log(a, 3))/3)) == a)
```

This function checks if the number given is greater than 0, then it checks if that number is equal to a power of 3 closest to it using `**` and `math.log()`. The expression `int(math.log(a, 3))/3` calculates the power to which the given number must be raised to obtain a cube. The `==` instead of `===` is intentional as the `math.log()` function has a small error margin.

To test this function you may use the following code:
```python
import unittest

class TestIsCube(unittest.TestCase):
    def test_iscube(self):
        self.assertTrue(iscube(1))
        self.assertTrue(iscube(-1))
        self.assertTrue(iscube(64))
        self.assertTrue(iscube(0))
        self.assertFalse(iscube(180))
        self.assertFalse(iscube(2))

    def test_edge_cases(self):
        self.assertTrue(iscube(0))
        self.assertTrue(iscube(1))
        self.assertTrue(iscube(-1))
        self.assertFalse(iscube(2))
        self.assertFalse(iscube(3))
        self.assertFalse(iscube(-2))
        self.assertTrue(iscube(8))
        self.assertTrue(iscube(27))
        self.assertFalse(iscube(28))

if __name__ == '__main__':
    unittest.main()
```

This code uses the `unittest` module to test the `iscube()` function with a variety of test cases including edge cases. 

If you are interested in more testing techniques and tools, please let me know.