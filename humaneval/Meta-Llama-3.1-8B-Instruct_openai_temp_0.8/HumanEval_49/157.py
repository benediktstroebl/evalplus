```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    :param n: exponent
    :param p: modulus
    :return: 2^n modulo p
    """
    def power(base: int, exponent: int, modulus: int) -> int:
        result = 1
        base = base % modulus
        while exponent > 0:
            if exponent % 2 == 1:
                result = (result * base) % modulus
            exponent = exponent // 2
            base = (base * base) % modulus
        return result

    return power(2, n, p)


# Test cases
print(modp(3, 5))  # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))  # 8
print(modp(100, 101))  # 1
```

This script uses a helper function called `power` to compute the power of a number modulo another number. It then uses this function to compute `2^n mod p`. The `power` function uses the exponentiation by squaring algorithm to efficiently compute the power. 

Note: This script avoids precision issues by using modular arithmetic. The `%` operator is used to reduce the base to its equivalent value modulo the modulus at each step.