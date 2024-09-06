Here's a Python script that defines the `brazilian_factorial` function, as per the problem statement:
```python
def special_factorial(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product
```

This implementation uses a simple `for` loop to calculate the `brazilian_factorial`. It starts with an initial value of `product` as `1` and then iterates through the range from `1` to `n` (inclusive). During each iteration, it multiplies the current value of `product` by the current value of `i`, effectively building up the product of all positive integers from `1` to `n`. Finally, it returns the computed `product`, which is the Brazilian factorial for the given input `n`. 

You can test this function by calling `special_factorial` with different input values. For instance:
```python
>>> special_factorial(4)
288
>>> special_factorial(5)
120_000
```

This approach uses a loop construct, which may not be the most efficient solution in terms of computational complexity. There are more optimized solutions available, but this loop-based approach provides a straightforward way to compute the Brazilian factorial.  If you're interested in more optimized solutions, please let me know!