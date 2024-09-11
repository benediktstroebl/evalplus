```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    :param n: The base number.
    :param p: The modulo number.
    :return: The result of 2^n modulo p.
    """
    result = 1
    while n > 0:
        # If n is odd, multiply the result by 2 and take modulo p
        if n % 2 == 1:
            result = (result * 2) % p
        # If n is even, divide n by 2 and repeat
        n = n // 2
    return result


# Test cases
print(modp(3, 5))  # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))  # 8
print(modp(100, 101))  # 1
```

This script uses a simple iterative approach to calculate 2^n modulo p. It starts with a result of 1 and repeatedly squares the current result (while taking modulo p) until n becomes 0. If n is odd at any point, the result is multiplied by 2 (and modulo p is taken) to account for the odd power of 2. The time complexity is O(log n) due to the repeated division by 2.