Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
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

The `count_up_to()` function iterates through numbers from 2 up to `n`, it checks each number using the `is_prime()` function to validate if it is a prime number. When a prime number is found and is less than `n`, it is added to the `primes` list. The loop stops when the `primes` list reaches `n` elements, thus providing the first `n` prime numbers under `n`. 

You can test this function by calling it with different input values to verify its behavior against the problem statement. 
For example:
```python
print(count_up_to(5)) # [2, 3]
print(count_up_to(11)) # [2, 3, 5, 7]
print(count_up_to(20)) # [2, 3, 5, 7, 11, 13, 17, 19]
print(count_up_to(0)) # []
print(count_up_to(1)) # []
print(count_up_to(18)) # [2, 3, 5, 7, 11, 13, 17]
``` 

This will help ensure that the function is producing the correct output for various input values.