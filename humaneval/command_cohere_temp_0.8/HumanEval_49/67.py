```python
def modp(n, p):
    return pow(2, n, p)
```

This Python expression employs the built-in `pow` function to calculate `2` raised to the power of `n` modulo `p`, leveraging the numerics of the latter for efficient modular exponentiation. 

Such a method is both concise and efficient, making it a strong choice for solving this specific problem. 

You can import this function into your code to test it: 

```python
import unittest

def modp(n, p):
    return pow(2, n, p)

class TestModp(unittest.TestCase):
    def test_modp(self):
        self.assertEqual(modp(3, 5), 3)
        self.assertEqual(modp(1101, 101), 2)
        self.assertEqual(modp(0, 101), 1)
        self.assertEqual(modp(3, 11), 8)
        self.assertEqual(modp(100, 101), 1)

if __name__ == '__main__':
    unittest.main()
```

This way, the `unittest` framework is leveraged to automatically run a set of specific tests that validate the behavior of the `modp` function. 

These tests aim to ensure that the function adheres to the problem's expected behavior by evaluating a variety of inputs and expected outputs. 

Overall, the included test suite serves as a crucial verification tool to confirm that the code works correctly. 

Any specific test case that you enact underneath the `test_modp` method will be incorporated into this test suite, enabling thorough examination of the function's robustness and functionality.