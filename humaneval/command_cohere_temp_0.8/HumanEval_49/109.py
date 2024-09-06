Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function accepts two integers as parameters, namely `n` and `p`. It then uses the `pow` function to calculate `2` to the power of `n` modulo `p`. This operation is performed to obtain the remainder when `2` is raised to the power of `n`, and then divided by `p`. This formula is commonly used in cryptography and modular mathematics.

Here is an example of its usage:
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
The given examples illustrate how the `modp` function can be used to compute the result of raising 2 to different powers modulo different prime numbers, and how it handles edge cases such as when `n` is zero.