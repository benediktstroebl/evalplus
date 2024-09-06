Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n integers that are prime numbers and less than n"""
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

The `count_up_to()` function iterates through numbers from 2 up to `n`, it checks each number using the `is_prime()` function to verify if it's a prime number and if it's less than `n`. If the criteria are met, the number is added to the `primes` list and the `count` variable is incremented. Once the `count` reaches the value of `n`, the function stops iterating and returns the `primes` list.

To verify that the implementation works, we can verify the previous example scenarios:
```python
print(count_up_to(5)) # [2,3]
print(count_up_to(11)) # [2,3,5,7]
print(count_up_to(20)) # [2,3,5,7,11,13,17,19]
print(count_up_to(0)) # []
print(count_up_to(1)) # []
print(count_up_to(18)) # [2,3,5,7,11,13,17]
```

This script will output the expected result for each of the provided examples. 

Note that the `is_prime()` function is a basic prime number checker and may not be suitable for use in other contexts or with much larger numbers. There are more efficient prime checks such as the `Sieve of Eratosthenes` that would be more suitable for larger ranges.