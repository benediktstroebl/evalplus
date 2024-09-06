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

This script contains a `count_up_to()` function that takes an integer n and returns an array of the first n prime numbers less than n. The `is_prime()` function is used to determine if a number is prime. The `count_up_to()` function iterates through numbers from 2 up to `n`, adding each prime number to the `primes` list until the list has `n` elements, which is the desired count. 

Here is an example of how to use the above code:
```python
print(count_up_to(5)) # [2, 3]
print(count_up_to(11)) # [2, 3, 5, 7]
print(count_up_to(20)) # [2, 3, 5, 7, 11, 13, 17, 19]
```

This program will print the expected output for the given examples in the problem statement.