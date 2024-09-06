```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function adheres to the problem statement by determining a number's primality, employing a brute-force approach via a loop that examines all integers from 2 up to the square root of the target number. If none of these divisors exist, the number is considered prime and the function returns `True`. Otherwise, it returns `False`. This method is not the most efficient approach for very large numbers, but it works well for the range of numbers covered by the provided tests.  This solution should pass all the test cases provided, including edge cases like `n = 1` and `n = 4`, and larger primes like `n = 61` and `n = 13441`.  This is a straightforward approach to solving the problem, but it might not be the most efficient for large numbers.  In such a case, more sophisticated algorithms like the Sieve of Eratosthenes would be more suitable.