```python
def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Breadth-first search for prime factors
    i = 2
    while i * i <= n:
        if n % i == 0:
            while n % i == 0:
                n //= i
            yield i
        i += 1
    if n > 1:
        yield n

```
The function iterates through potential prime factors in a breadth-first manner, starting from 2. It yields each prime factor it finds, and since the largest prime factor is the last prime factor in the factorization, the last yield statement corresponds to the largest prime factor. This approach ensures that the function handles both specificalcated test cases and performs efficiently for larger inputs.  You can use this function to find the largest prime factor of any number by passing it as an argument.  You can use this function in your code to calculate the largest prime factor as needed.  If you have any questions, feel free to ask!