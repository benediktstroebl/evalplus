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
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n."""
    count = 0
    primes = []
    for num in range(2, n+1):
        if is_prime(num) and num < n:
            primes.append(num)
            count += 1
            if count == n:
                break
    return primes
```

The `count_up_to()` function iterates through numbers from 2 up to `n`, it checks each number using the `is_prime()` function to verify if it's a prime number and if it's less than `n`. If it is a prime number, it is added to the `primes` list and the `count` variable is incremented. Once the `count` variable reaches the value of `n`, the loop is terminated and the list of prime numbers is returned.

Here is an example of how to use the `count_up_to()` function to count up to `n` to be specified:
```python
print(count_up_to(5)) # [2, 3]
print(count_up_to(11)) # [2, 3, 5, 7]
print(count_up_to(20)) # [2, 3, 5, 7, 11, 13, 17, 19]
```

The `is_prime()` function is also available to verify if a number is prime, here is an example of how to use it:
```python
print(is_prime(2)) # True
print(is_prime(3)) # True
print(is_prime(4)) # False
```

This script solves the problem in a straightforward way, with clear and modular code that should be easily understandable and maintainable.