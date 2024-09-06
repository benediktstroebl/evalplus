Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function defines the `modp` function which takes in two integers `n` and `p` and returns `2` raised to the power of `n` modulo `p`. This is accomplished by using the built-in Python function `pow` in combination with the modulo operator `%`. 

To use this script, you can copy and paste it into a Python environment or script file, and then call the `modp` function with the arguments `n` and `p`.  Please note that this approach may produce incorrect results when `p` is large or when `n` is large enough for the result to exceed the prime's size, due to numerical issues. You may want to consider alternative implementations for specific cases.