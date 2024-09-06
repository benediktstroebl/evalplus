```python
def modp(n, p):
    return pow(2, n, p)
```

This function `modp(n, p)` computes `2^n` modulo `p` using the built-in function `pow(x, y, p)`. This efficiently calculates the exponentiation `x^y` modulo `p` directly. The function then returns the result which is the remainder after dividing the exponentiated value by `p`. 

This solution is concise and leverages Python's built-in optimizations for modular exponentiation, resulting in a time complexity of O(log(n)) for calculating `2^n` modulo `p`. 

This approach easily handles various edge cases including negative `n` or composite values for `p`.