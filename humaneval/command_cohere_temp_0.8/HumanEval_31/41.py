Here's a Python script with a self-contained function that solves the prime-checking problem:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function is crafted to efficiently determine whether a given number n is prime. It begins by handling the special case of n being less than 2, returning False as such. Then, it iterates from 2 up to the square root of n, checking if n is divisible by any integer in this range. If any divisors are found, the function returns False, indicating that the number is not prime. However, if no divisors are encountered, the function returns True, indicating that the number is prime. This approach combines simplicity and efficiency, enabling the swift and accurate verification of primality for testing.