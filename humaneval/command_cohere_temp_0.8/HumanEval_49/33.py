Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function accepts two integers as parameters, namely `n` and `p`. It utilizes the `pow` function to compute `2` raised to the power of `n` modulo `p`, thereby returning the result.

To test this function, you can execute the following code:
```python
>>> modp(3, 5)
3
>>> modp(1101, 101)
2
>>> modp(0, 101)
1
>>> modp(3, 11)
8
>>> modp(100, 101)
1
```

The given example tests illustrate correct functionality of the `modp` function. These tests demonstrate the calculation of the powers of 2 modulo a prime number `p`, handling both positive and zero `n` values as well as demonstrating awareness of numerical issues.