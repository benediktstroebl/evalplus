```python
def modp(n, p):
    return pow(2, n, p)
```

This function `modp(n, p)` computes `2^n % p` by leveraging the built-in function `pow()`. This optimizes the process of computing exponentiation and modular operations, as shown by the following test cases:
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

It's crucial to remember that the `pow()` method has simplified the process by calculating the exponentiation and modular operation in a single step, eliminating the need for extra variables. This makes the code more straightforward and easier to comprehend. If you desire a more comprehensive explanation, please let me know!