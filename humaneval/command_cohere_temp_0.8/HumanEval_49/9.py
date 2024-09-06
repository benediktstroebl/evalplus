Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function defines the `modp` function which calculates `2^n modulo p` using the built-in `pow` function and returns the result. 

To use this function, you can call it with two arguments: `n`, which is the exponent, and `p`, which is the modulus. For example:
```python
print(modp(3, 5))  # Outputs 3
print(modp(1101, 101))  # Outputs 2
print(modp(0, 101))  # Outputs 1
print(modp(3, 11))  # Outputs 8
print(modp(100, 101))  # Outputs 1
```
This demonstrates the function's behavior and its expected output for the given test cases.