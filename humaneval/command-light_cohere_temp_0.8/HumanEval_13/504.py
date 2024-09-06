```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both numbers must be set")
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both numbers must be integers")
    if a <= 0 or b <= 0:
        raise ValueError("Both numbers must be positive")
    if a == 0 and b == 0:
        return 0
    
    # prime factorization and divisor calculation
    prime_factors = ((2 * i + 1) ** min(i, 5) for i in range(1, max(a, b) + 1) if a % i == 0 and b % i == 0)
    
    divisor = max(prime_factors)
    
    # ensure divisibility remains valid
    if any(i > a or i > b for i in prime_factors):
        divisor = 0
    
    return divisor
```