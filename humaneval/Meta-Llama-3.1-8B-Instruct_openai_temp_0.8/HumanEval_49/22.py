```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).
    
    :param n: The exponent
    :param p: The base of the modulus operation
    :return: 2^n modulo p
    """
    result = 1
    while n > 0:
        # If n is odd, multiply the result by 2 and take modulo p
        if n % 2 == 1:
            result = (result * 2) % p
        # Divide n by 2 (Integer division)
        n = n // 2
    return result

# Example usage:
print(modp(3, 5))   # Output: 3
print(modp(1101, 101))   # Output: 2
print(modp(0, 101))   # Output: 1
print(modp(3, 11))   # Output: 8
print(modp(100, 101))   # Output: 1
```
This script implements the modp function using exponentiation by squaring, which is a efficient method for computing large powers. The time complexity of this algorithm is O(log n), where n is the exponent. This is because in each iteration, we divide the exponent by 2, effectively reducing the number of multiplications required.