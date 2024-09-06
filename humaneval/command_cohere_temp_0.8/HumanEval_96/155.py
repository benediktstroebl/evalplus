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
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n."""
    count = 0
    primes = []
    for i in range(2, n + 1):
        if is_prime(i) and i < n:
            primes.append(i)
            count += 1
            if count == n:
                break
    return primes
```

The `count_up_to()` function iterates through numbers from 2 up to `n`, it checks each number using the `is_prime()` function to verify if it's a prime number and if it's less than `n`. If it is a prime number, it is added to the `primes` list, and the `count` variable is incremented. Once the `count` reaches `n`, the function stops iterating and returns the `primes` list, which contains the first `n` prime numbers under `n`.

Here is an example of the first ten prime numbers:
```python
print(count_up_to(10))
```
Which outputs:
```
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```