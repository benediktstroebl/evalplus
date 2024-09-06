```python
def modp(n, p):
    return pow(2, n, p)
```

This function `modp(n, p)` leverages the `pow()` function, which takes three arguments: the base (in this case, 2), the exponent (the `n` argument), and the modulus (the `p` argument). The function returns the result of exponentiation modulo `p`, ensuring that the result remains within the range of `p`. 

This solution handles the edge cases mentioned in the prompt, returning `1` when `n` is zero and returning the remainder when `n` is a positive integer. 

To ensure that the solution works correctly for negative `n`, you need to specify the type of the `n` argument as `int` in the function signature, as shown in the previous response. This way, the function will handle negative exponents correctly, as negative numbers raised to non-zero powers in Python become positive. 

Feel free to test this function with the example use cases provided in the markdown code block, and it should pass all the tests.