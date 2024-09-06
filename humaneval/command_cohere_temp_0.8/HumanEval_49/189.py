```python
def modp(n, p):
    return pow(2, n, p)
```

This Python script defines a function `modp` that takes in two integers `n` and `p` and returns `2^n modulo p` using the `pow` function, which returns the result of raising the first argument (`2` in this case) to the power of the second argument (`n`) and multiplying it by the third argument (`p`) and taking the modulo `p`. 

This function is designed to handle various input scenarios and provides the corresponding result based on these operations' mathematical properties.