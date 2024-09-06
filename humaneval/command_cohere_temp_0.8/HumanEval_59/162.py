```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for the largest possible factor numerically
    largest_factor = n // 2
    while True:
        if n % 2 == 0:
            n //= 2
        else:
            break
    # Iterate through possible divisors 2 times the largest factor
    for i in range(3, largest_factor * 2 + 1, 2):
        while n % i == 0:
            n //= i
            if i == largest_factor:
                return i
            elif i > largest_factor:
                largest_factor = i
    if n > 1:
        return n
```
The provided Python script defines a function `largest_prime_factor(n)` that calculates the largest prime factor of a given number `n`. It starts by dividing `n` by 2 repeatedly until it becomes odd. Then, it iterates through potential divisors starting from 3 up to twice the largest factor found so far (the loop ranges from 3 to `largest_factor * 2 + 1`, progressing in steps of 2). It systematically eliminates all divisors except for the largest prime factor, ensuring an efficient computation. The function returns the largest prime factor, or `n` if it's odd and not a prime. The code efficiently identifies the largest prime factor without the need for factoring all numbers from 2 to `n`.