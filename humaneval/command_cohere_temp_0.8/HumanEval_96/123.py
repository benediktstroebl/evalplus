```python
def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n."""
    count = 0
    primes = []
    for i in range(2, n+1):
        if is_prime(i) and i < n:
            primes.append(i)
            count += 1
            if count == n:
                break
    return primes
```

The `is_prime` function checks if a given number is prime or not. Then the `count_up_to` function generates a list of prime numbers less than or equal to `n` and returns the list once it has counted up to `n` primes, or if it has gone through all the prime numbers less than `n`. 

Here is an example of how to use the script to solve the problem:
```python
print(count_up_to(5)) # [2, 3]
print(count_up_to(11)) # [2, 3, 5, 7]
print(count_up_to(20)) # [2, 3, 5, 7, 11, 13, 17, 19]
```

This script will output the required list of primes up to the specified number. Would you like to know more about prime numbers or other related mathematical concepts? Just ask!