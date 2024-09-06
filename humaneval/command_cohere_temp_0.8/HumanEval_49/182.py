```python
def modp(n, p):
    return pow(2, n, p)
```

This script defines a Python function called `modp` that takes two integers `n` and `p` as input. It uses the built-in Python function `pow` to compute `2` raised to the power of `n` modulo `p`. This operation is commonly used in number theory and cryptography to perform calculations involving modular arithmetic. 

The function is designed to handle various scenarios and adheres to the problem statement's guidelines, including returning `1` when `n` is `0` or handling scenarios where `p` is prime. 

The function's behavior corresponds to the test cases provided in the problem statement. However, it's recommended to independently test the function with various inputs to ensure its correctness across different scenarios.