Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function defines the `modp` function, which takes in two integers `n` and `p`, and returns `2` raised to the power of `n` modulo `p`. This expression has a chance of overflowing unless we ensure that the result is numerically bounded by `p`. 

To do this, it uses the `pow` function, which returns `x` raised to the power of `y` modulo `z`, where each of these three arguments are integers. As per the Python documentation, `pow` uses the exponentiation-by-squaring algorithm, which is more efficient than the straightforward repeated multiplication of `x` by `y` (slow multiplication). It also neatly encapsulates the modulo operation into the expression, taking care of the concern you raised in the prompt. 

This function elegantly solves the problem in a single expression, providing a straightforward way to handle the modular exponentiation operation. 

This approach provides a concise solution that is both efficient and easy to understand, making it a useful tool for solving similar problems in the future.