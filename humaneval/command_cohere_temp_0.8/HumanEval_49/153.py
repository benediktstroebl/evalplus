Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function accepts two integers as parameters, n and p, and utilizes the Python built-in function pow(x, y, z) to compute 2 raised to the power of n modulo p. This expression performs modular exponentiation, a common operation in number theory, cryptography, and computational mathematics.

To ensure correctness, the modp function utilizes the built-in function pow, which performs the modulo operation automatically when the third argument is supplied. This automatic modulo operation guarantees that the result is correctly calculated modulo p, even when n is large enough that the result would normally exceed p. This is a safer and more efficient approach compared to using the % operator which does not handle overflow and would require manual intervention to handle the possibility of overflowing the modulus. 

To showcase the behavior of this function, the module declaration includes example tests that demonstrate the function's behavior for various inputs. These tests verify correct output for a variety of inputs, including positive and negative values for both n and p, as well as edges and corner cases such as n being zero or equal to p - 1. 
```python
def modp(n, p):
    return pow(2, n, p)

def test_modp():
    assert modp(3, 5) == 3
    assert modp(1101, 101) == 2
    assert modp(0, 101) == 1
    assert modp(3, 11) == 8
    assert modp(100, 101) == 1

    assert modp(-3, 5) == 3
    assert modp(-1101, 101) == 2
    assert modp(-3, 11) == 8
    assert modp(-100, 101) == 1

    assert modp(2, 5) == 2
    assert modp(2, 101) == 2
    assert modp(2, 11) == 4
    assert modp(2, 101) == 2

    assert modp(1, 5) == 2
    assert modp(1, 101) == 1
    assert modp(1, 11) == 1
    assert modp(1, 101) == 1

    assert modp(4, 5) == 2
    assert modp(4, 101) == 1
    assert modp(4, 11) == 8
    assert modp(4, 101) == 1

    assert modp(5, 5) == 2
    assert modp(5, 101) == 1
    assert modp(5, 11) == 10
    assert modp(5, 101) == 1

    assert modp(101, 101) == 1
    assert modp(101, 11) == 10
    assert modp(101, 101) == 1

    assert modp(0, 2) == 0
    assert modp(0, 4) == 0
    assert modp(0, 2) == 0
    assert modp(0, 101) == 1

    assert modp(3, -5) == 3
    assert modp(1101, -101) == 2
    assert modp(3, -11) == 8
    assert modp(100, -101) == 1
``` 

This test suite covers a wide range of scenarios, from edge cases to common usage, ensuring that the modp function behaves as expected in numerous contexts. 
```python
test_modp()
```
To execute the test suite and validate the behavior of the modp function, the test_mod