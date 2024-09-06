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

The `count_up_to()` function iterates through integers from 2 up to `n`, it checks each integer with the `is_prime()` function. If it's a prime number and less than `n`, it's added to the `primes` list. The loop stops when `count` reaches `n` or when it reaches `n+1`.

You can test this code snippet by adding a test case for each edge case in the function signature above. 

For example: 
```python
count_up_to(5) == [2, 3]
count_up_to(11) == [2, 3, 5, 7]
count_up_to(0) == []
count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]
count_up_to(1) == []
count_up_to(18) == [2, 3, 5, 7, 11, 13, 17]
```

This will help ensure that the function is correct and properly handles all edge cases.