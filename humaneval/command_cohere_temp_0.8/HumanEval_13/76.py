```python
def greatest_common_divisor(a, b) -> int:
    """ Returns the greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```
This code defines a recursive function `greatest_common_divisor` that returns the greatest common divisor of two integers `a` and `b`. It utilizes the Euclidean algorithm to find the GCD. If `a` is 0, it returns `b` as an edge case where `b` may be the GCD. 

Here is a snippet of a test file that can be used to verify the functionality of the code:
```python
import unittest

def greatest_common_divisor(a, b) -> int:
    """ Returns the greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)

class TestGreatestCommonDivisor(unittest.TestCase):
    def test_gcd_1(self):
        self.assertEqual(greatest_common_divisor(3, 5), 1)

    def test_gcd_2(self):
        self.assertEqual(greatest_common_divisor(25, 15), 5)

    def test_gcd_3(self):
        self.assertEqual(greatest_common_divisor(0, 15), 15)

    def test_gcd_4(self):
        self.assertEqual(greatest_common_divisor(10, 0), 0)

if __name__ == '__main__':
    unittest.main()
```
This test file contains four test functions (`test_gcd_1`, `test_gcd_2`, `test_gcd_3`, and `test_gcd_4`) that cover different scenarios. 
The `unittest.main()` call allows the running of the tests when the script is executed directly. 

To execute the test file, ensure that the `greatest_common_divisor` function is saved in a separate Python file and that both files are in the same directory. You can then run the test file using the following command:
```bash
python test_greatest_common_divisor.py
```
Running this command will execute the test file, and any failures or errors will be printed to the console, along with the number of tests passed.