## Computing 2^n Mod p
### Problem Description
Calculate 2^n modulo p efficiently using Python.

### Solution
```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p.

    Note: This function is optimized to handle large inputs by using the property
    of modular arithmetic that (a*b) % p = ((a % p) * (b % p)) % p.

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
    """
    result = 1
    while n > 0:
        if n % 2 == 1:
            result = (result * 2) % p
        n = n // 2
    return result
```

### Explanation

This function uses a technique called exponentiation by squaring to efficiently compute 2^n modulo p. The idea is to break down the exponent n into its binary representation, and then use the properties of modular arithmetic to compute the result.

Here's how it works:

1. We initialize the result to 1.
2. We loop until n is 0.
3. In each iteration, we check if n is odd (i.e., n % 2 == 1). If it is, we multiply the result by 2 modulo p.
4. We divide n by 2.
5. We repeat steps 3-4 until n is 0.
6. We return the final result.

This algorithm has a time complexity of O(log n), making it efficient for large inputs.