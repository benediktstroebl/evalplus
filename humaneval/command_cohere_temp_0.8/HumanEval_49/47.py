Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function accepts two integers as parameters, namely `n` and `p`. It then uses the `pow` function to calculate `2` raised to the power of `n` modulo `p`. This operation is useful in various mathematical and cryptographic applications, especially when working with modular arithmetic.

Here is an example of how you can use the function:
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
The given examples illustrate how the `modp` function can be used to compute 2^n modulo p for various values of n and p. Each result is a single integer.