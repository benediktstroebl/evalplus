```python
def modp(n, p):
    return pow(2, n, p)
```

This function `modp(n, p)` uses the `pow` function to calculate `2` raised to the power of `n` modulo `p`. It's a direct solution that fulfills the problem's requirement. 

To ensure that the script works correctly, three test cases are added below, which are inspired by the given example scenarios. These test cases help verify if the function behaves as expected.

```python
# Testing the modp function
import unittest

def modp(n, p):
    return pow(2, n, p)

class TestModpFunction(unittest.TestCase):
    def test_modp_example_1(self):
        self.assertEqual(modp(3, 5), 3)

    def test_modp_example_2(self):
        self.assertEqual(modp(1101, 101), 2)

    def test_modp_example_3(self):
        self.assertEqual(modp(0, 101), 1)

    def test_modp_example_4(self):
        self.assertEqual(modp(3, 11), 8)

    def test_modp_example_5(self):
        self.assertEqual(modp(100, 101), 1)

if __name__ == '__main__':
    unittest.main()
```

To run the test suite, the command `python test_modp.py` can be used. 

This complete script demonstrates a straightforward solution to the problem and includes tests to ensure that the solution remains valid for various cases. 

*Note*: Be cautious of numerical issues when dealing with modular arithmetic, and consider utilizing preconceptions to make code more efficient and concise.