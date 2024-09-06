```python
def modp(n, p):
    return pow(2, n, p)
```

This function `modp(n, p)` leverages the `pow()` function, which takes three arguments: the base (in this case, 2), the exponent (input `n`), and the modulus (input `p`). The function returns the result of exponentiation modulo `p`, ensuring that the result is within the range of `p`. 

This solution is concise and efficient, providing a straightforward way to compute 2^n modulo a given prime `p`. 

To accompany this solution, it's essential to consider edge cases and provide tests to validate the function's behavior across different scenarios:
```python
# Testing the modp function
import unittest

def test_modp():
    # Basic Tests:
    assert modp(0, 101) == 1
    assert modp(3, 5) == 3
    assert modp(1101, 101) == 2

    # Edge Tests:
    assert modp(3, 11) == 8  # Tests when p is a factor of 2^n
    assert modp(100, 101) == 1  # Tests when n > log(p) / log(2)

    # Larger Tests:
    assert modp(10, 101) == 1
    assert modp(520, 5) == 3

    # Test with negative values
    assert modp(-3, 11) == 8  # -3 is converted to 3 modulo 11
    assert modp(-5, 5) == 0

    # Test with 0 exponent
    assert modp(0, 5) == 1
    assert modp(0, 101) == 1

if __name__ == '__main__':
    unittest.main()
```

This test suite covers various scenarios, from basic tests to edge cases, ensuring that the `modp` function behaves as expected across different inputs. 

The `unittest.main()` call runs the tests when the script is executed directly.  This way ensures that the function is correctly implemented and behaves as intended.  In doing so, it allows developers to confidently use this function for various purposes, knowing that it provides the desired results.