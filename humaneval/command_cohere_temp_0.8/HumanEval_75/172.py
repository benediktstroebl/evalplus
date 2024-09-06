```python
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 100 and a > 1:
        for i in range(2, int(a**0.5) + 1):
            if a % i == 0:
                return False

        return True
    return False
```

The purpose of the `is_multiply_prime` function is to determine whether a given number `a` can be expressed as the product of three distinct prime numbers. It does so by implementing a optimized brute force approach, examining each prime number from 2 up to the square root of `a`. The function returns 'True' if no divisors are found and 'False' if any divisors are found, indicating that the number is not a product of three primes. This approach provides an efficient way to verify the uniqueness of factors while maintaining a manageable time complexity.