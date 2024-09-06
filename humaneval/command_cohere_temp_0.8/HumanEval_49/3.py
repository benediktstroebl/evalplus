Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function accepts two integers as arguments, namely `n` and `p`. It then returns `2` raised to the power of `n` modulo `p` by leveraging the `pow` function. This solution accounts for the issue of numerics and efficiently computes the result. 

Here is a test suite to ensure the function operates correctly:
```python
def test_modp():
    assert modp(3, 5) == 3
    assert modp(1101, 101) == 2
    assert modp(0, 101) == 1
    assert modp(3, 11) == 8
    assert modp(100, 101) == 1
```
This test suite includes various inputs to validate the correct operation of the `modp` function.