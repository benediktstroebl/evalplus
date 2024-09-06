```python
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    prime_factors = []
    for i in range(2, int(a ** 0.5) + 1):
        while a % i == 0:
            prime_factors.append(i)
            a //= i
        if a == 1:
            break
    return len(prime_factors) == 3
```

The function 'is_multiply_prime' determines whether or not the given number is the product of three prime integers less than 100. It does this by first determining the prime factors of the number and then counting the number of prime factors. The algorithm returns True if the count is three, otherwise False. The function is implemented using an optimized approach that reduces the search space iteratively.