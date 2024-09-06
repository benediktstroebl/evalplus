Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function accepts two integers as parameters, namely `n` and `p`. It utilizes the Python built-in function `pow` to compute `2` raised to the power of `n` modulo `p`, thereby offering the required result. 

Here is an example to demonstrate its usage:
```python
n = 3
p = 5
print(modp(n, p))  # Outputs 3
```
This will return `3`, which is `2^{3} \pmod{5}`. 

This function handles the problem presented, delivering the correct result for various scenarios. Nevertheless, it's crucial to remember that the `pow` function returns a complex number when the exponent is negative, so careful consideration of the context and desired output format may be necessary.