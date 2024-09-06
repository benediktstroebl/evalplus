```python
def modp(n, p):
    return pow(2, n, p)
```

This function takes two inputs, `n` and `p`, and returns `2` raised to the power of `n` modulo `p` using the `pow` function. It is a direct implementation of the problem statement without additional logic or considerations.

Here is a sample output using the function with different test cases:
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

This function is straightforward and effective, providing a simple way to compute the result for various inputs while maintaining correct markdown documentation. Feel free to adapt and extend it to suit your needs. If you have further questions or need more assistance, let me know!