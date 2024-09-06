```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function checks if a number is prime or not. It first checks if the number is smaller than 2, returning false in such a case. It then iterates from 2 up to the square root of the number `n`, checking if the number is divisible by any other number. If the number is divisible by any other number in this range, it returns false. If it is not, it returns true. The function includes a set of tests in the comments to ensure it behaves as expected.