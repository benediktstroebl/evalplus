Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function defines the `modp` function which takes in two integers `n` and `p` and returns `2^n modulo p` using the built-in `pow` function and appropriately passes the modulo argument `p`. 
It assumes that the inputs are valid and that `n` is a non-negative integer. 
If you're looking for more detailed explanations and derivations of the solution or want to learn more about number theory, feel free to ask!