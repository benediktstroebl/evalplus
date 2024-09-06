```python
def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_up_to(n):
    """Return the first n prime numbers less than n"""
    count = 0
    primes = []
    for num in range(2, n + 1):
        if is_prime(num) and num < n:
            primes.append(num)
            count += 1
            if count == n:
                break
    return primes
```

This code contains two functions. The `is_prime` function checks if a given number is prime or not in logarithmic time. The `count_up_to` function generates a list of the first `n` prime numbers less than `n` by iterating through all numbers from 2 to `n` and selecting only the prime numbers. 

Here is an example of how to use this code:
```python
print(count_up_to(5))  # [2, 3]
print(count_up_to(11))  # [2, 3, 5, 7]
print(count_up_to(20))  # [2, 3, 5, 7, 11, 13, 17, 19]
```

This code should correctly solve the problem for all input values, and will be efficient for large inputs since the `is_prime` function uses a logarithmic iteration mechanism.