Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function defines the `modp` function which calculates `2^n modulo p` using the built-in `pow` function and returns the result. The script contains no external dependencies or additional code.  It relies solely on the Python built-in functions to solve the problem. 
The function is implemented elegantly and efficiently, allowing straightforward calculations of `2^n modulo p` without any manual looping or explicit modular arithmetic operations. 

This solution assumes that no explicit output is required, as the function simply returns the result of the expression 'pow(2, n, p)'. If the goal is to print the result for visualization purposes, a print statement can be added to the function, 
For example: 

```python
def modp(n, p):
    result = pow(2, n, p)
    print(f"2^{n} modulo {p}: {result}")
    return result
```
This adds a print statement to the function to showcase the result for verification.