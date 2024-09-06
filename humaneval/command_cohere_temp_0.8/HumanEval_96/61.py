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

The `count_up_to()` function iterates through integers between 2 and `n`, it checks each integer with the `is_prime()` function. If it's a prime number and less than `n`, it's added to the `primes` list. The `count` variable keeps track of how many primes have been found and stops the loop once `count` reaches `n`, meaning the `primes` list now contains the first `n` prime numbers less than `n`.

Here's an example of how you can call the function to test it out:
```python
print(count_up_to(5)) # [2, 3]
print(count_up_to(11)) # [2, 3, 5, 7]
print(count_up_to(20)) # [2, 3, 5, 7, 11, 13, 17, 19]
print(count_up_to(18)) # [2, 3, 5, 7, 11, 13, 17]
print(count_up_to(0)) # []
print(count_up_to(1)) # []
```

This will output the expected result for each example provided in the problem statement.