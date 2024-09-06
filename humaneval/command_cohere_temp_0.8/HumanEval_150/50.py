```python
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def x_or_y(n, x, y):
    if is_prime(n):
        return x
    else:
        return y

# Test cases
print(x_or_y(7, 34, 12))  # Output: 34
print(x_or_y(15, 8, 5))  # Output: 5
```

This script defines a function `x_or_y` that takes three arguments: `n` (which is supposedly a prime number), `x`, and `y`. If `n` is prime, the function returns `x`, else it returns `y`.

To check if `n` is prime, the function uses a simple algorithm:
1. If `n` is less than or equal to 1, it's not prime.
2. If `n` is equal to 2 or 3, it's prime. These are the smallest prime numbers.
3. If `n` is divisible by 2 or 3, it's not prime.
4. Check for divisibility by odd numbers starting from 5 up to the square root of `n`.

The function is_prime(7) returns True, so the x_or_y(7, 34, 12) call returns 34. Similarly, is_prime(15) returns False, so x_or_y(15, 8, 5) returns 5.