```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function `is_prime(n)` determines if a given number is prime or not. It begins by handling the case where `n` is less than 2, returning `False` in such cases. The function then starts a loop from 2 to the square root of `n`, incrementing by 1 each time. If the number `i` in the loop's iteration divides `n` without leaving a remainder, indicating that `n` is not a prime number, the function returns `False`. If none of these conditions are met by the loop's conclusion, the function returns `True`, indicating that the given number is prime. This approach enables the function to efficiently determine whether a number is prime or not.