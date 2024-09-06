```python
def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Make a list of the prime factors of n
    pf = []
    while n % 2 == 0:
        pf.append(2)
        n = n / 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            pf.append(i)
            n = n / i
    if n > 2:
        pf.append(n)
    # Return the largest element of the list
    return max(pf)
```

The function largest_prime_factor() takes an integer n as input and returns the largest prime factor of n. This assumes that n is greater than 1 and is not a prime number.

The process is achieved as follows:
1. Initially, a blank list named pf is created to hold the prime factors of n.
2. The loop continues iterating through even numbers (starting from 2) listed in `n` until it becomes 1. It calculates divisibility and appends 2 as a prime factor to the `pf` list at each step where `n` is even.
3. The loop then iterates through odd numbers (starting from 3) up to the square root of `n`, incrementing by 2 each time. It calculates divisibility and appends each applicable odd number to the `pf` list.
4. If `n` surpasses 2 and isn't represented in the `pf` list, it is appended as the final step since primality is assumed.
5. Finally, the function returns the maximum (largest prime factor) of the `pf` list.

This approach ensures that the prime factors of `n` are correctly identified and the largest prime factor is accurately returned, considering the assumptions provided.