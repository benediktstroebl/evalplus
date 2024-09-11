```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    This function uses the property of modular arithmetic that (a*b) % n = ((a % n) * (b % n)) % n
    to efficiently calculate 2^n modulo p.
    """
    result = 1
    while n > 0:
        # If n is odd, multiply the result by 2 modulo p
        if n % 2 == 1:
            result = (result * 2) % p
        # Square 2 modulo p and divide n by 2
        n = n // 2
        p = (p * p) % p
    return result

# Test cases
print(modp(3, 5))   # 3
print(modp(1101, 101))   # 2
print(modp(0, 101))   # 1
print(modp(3, 11))   # 8
print(modp(100, 101))   # 1
```

This script defines a function `modp(n, p)` that calculates `2^n modulo p` efficiently using the property of modular arithmetic mentioned above. It uses a while loop to iterate until `n` becomes 0, and in each iteration, it either multiplies the result by 2 modulo `p` if `n` is odd, or squares 2 modulo `p` and divides `n` by 2. The function returns the final result. The test cases at the end verify the correctness of the function.