Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This straightforward function leverages the built-in `pow` function to calculate `2` raised to the power of `n` modulo `p`, altogether solving the posed problem. 

Here's a test suite that can be used to validate the function against the examples provided:
```python
def test_modp():
    assert modp(3, 5) == 3
    assert modp(1101, 101) == 2
    assert modp(0, 101) == 1
    assert modp(3, 11) == 8
    assert modp(100, 101) == 1
```
Executing this test suite will affirm that the `modp` function conforms with the problem statement and behaves as expected. 

This solution assumes `p` is a prime number. For a more general result for modular exponentiation, see the `pow(x, y, m)` function in Python's documentation.