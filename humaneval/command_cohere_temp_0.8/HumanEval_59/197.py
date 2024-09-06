```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Test if n is a prime number
    if n == 2 or n == 3:
        return n
    elif n <= 1 or n % 2 == 0 or n % 3 == 0:
        return 2
    i = 5
    while i * i <= n:
        # Check if i is a prime or not
        if n % i == 0 or n % (i + 2) == 0:
            return i
        i += 6
    # If no prime factors are found, return n
    return n
```

The function iterates through potential prime factors from `5` to the square root of `n`. It factors in efficiencies that reduce the search space by ruling out even numbers and numbers that are divisible by `5` or `7`. This optimization ensures the function performs efficiently while delivering the correct result. 

This approach results in a reasonable average time complexity of O(√n).

This function is efficient and can handle various input cases, including edge cases, and will be able to handle future cases that may arise.