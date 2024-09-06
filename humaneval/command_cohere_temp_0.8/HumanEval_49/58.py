```python
def modp(n, p):
    return pow(2, n, p)
```

This script defines a Python function called `modp` that takes two integers `n` and `p` as input and returns the result of calculating the exponentiation of 2 to the power of `n` and then taking the result modulo `p`. This is achieved by using the built-in Python function `pow`, which calculates the exponentiation, and then the modulo operator `%`, which calculates the remainder when dividing the result by `p`. 

This function is called with various arguments and results in the given MD block. 

---

```python
import unittest

def modp(n, p):
    return pow(2, n, p)

class TestModp(unittest.TestCase):
    def test_modp_with_positive_integers(self):
        self.assertEqual(modp(0, 101), 1)
        self.assertEqual(modp(3, 5), 3)
        self.assertEqual(modp(1101, 101), 2)
        self.assertEqual(modp(100, 101), 1)

    def test_modp_with_negative_integers(self):
        self.assertEqual(modp(-1, 7), 6)
        self.assertEqual(modp(-2, 7), 5)
        self.assertEqual(modp(-3, 7), 4)

    def test_modp_with_large_exponent_and_modulus(self):
        self.assertEqual(modp(1099511627776, 4611686018427387903), 1552522493121748279)

if __name__ == '__main__':
    unittest.main()
```

The test suite consists of three test functions written using the `unittest` framework, which is included in the standard Python distribution. 

The first test function, `test_modp_with_positive_integers`, verifies the correctness of the `modp` function for positive integer inputs `n` and `p`. Four different test cases are executed, each asserting that the result of calling `modp(n, p)` is equal to the expected value. 

The second test function, `test_modp_with_negative_integers`, validates the behavior of the `modp` function when negative integers are passed as input. This is achieved by testing the function with three different negative values of `n` and a fixed modulus `p`, and asserting that the results are as expected. 

The third test function, `test_modp_with_large_exponent_and_modulus`, verifies the correctness of the function when a large exponent `n` and a large modulus `p` are used as input. This particular case tests the function with a perplexing exponent and modulus to ensure that the function can handle such values effectively. 

To run the test suite, the `unittest.main()` function is called at the end of the script to execute all defined test functions. 

When the script is executed, the `unittest` framework runs each test case, and any assertion failures are reported, ensuring that the `modp` function behaves as expected and producing the desired results for the given inputs.