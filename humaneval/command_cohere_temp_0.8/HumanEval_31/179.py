Here's a Python script with a self-contained function `is_prime` that follows the problem statement and hopefully passes the tests provided:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function checks if a given number `n` is less than 2, returns `False`. If `n` is greater than 1, it iterates from 2 to the square root of `n` (inclusive), and for each number `i`, it checks if `n` is divisible by `i`. If there is a divisor, it returns `False`. If no divisors are found after the loop, it returns `True`.

The provided tests should make sure that this function behaves as expected:
```python
# Testing the is_prime function
>>> is_prime(6)
False
>>> is_prime(101)
True
>>> is_prime(11)
True
>>> is_prime(13441)
True
>>> is_prime(61)
True
>>> is_prime(4)
False
>>> is_prime(1)
False
```

Let's take a quick look at how the function works:
- It handles the edge case where `n` is less than 2 by returning `False`.
- Then, it checks if the number is divisible by any number from 2 to the square root of `n`. A divisor is found if the current number `i` divides `n` without any remainder.
- If no divisor is found, it means `n` is prime, and the function returns `True`.

This approach uses a simple optimization by checking only up to the square root of `n`. It's an optimization because it's known that if `n` has no divisors within the range `2 <= i <= sqrt(n)`, it won't have any divisors elsewhere. This is a prime-checking technique often used in algorithms.