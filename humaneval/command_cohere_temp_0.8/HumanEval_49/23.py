Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function defines the modp function which takes in two integers n and p and returns 2 raised to the power of n modulo p. This is accomplished by using the built-in function pow which takes in the base, exponent, and modulus as arguments and returns the value of the base raised to the power of the exponent modulo the modulus. 

To test this function, you can call it with different inputs and compare the results to the expected output. 

For example:
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
Output: