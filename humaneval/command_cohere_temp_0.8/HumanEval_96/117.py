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

The function `is_prime` is used to check if a number is prime. 
The function `count_up_to` begins testing numbers from 2 and stores each prime number that is less than `n` in the `primes` list. The loop stops when `count` reaches `n`, or when a number greater than `n` is encountered.

Here is a usage example to test the function:
```python
print(count_up_to(5))  # [2, 3]
print(count_up_to(11))  # [2, 3, 5, 7]
print(count_up_to(20))  # [2, 3, 5, 7, 11, 13, 17, 19]
print(count_up_to(18))  # [2, 3, 5, 7, 11, 13, 17]
print(count_up_to(0))   # []
print(count_up_to(1))   # []
``` 

The aforementioned example test cases should output the following:
```
[2, 3]
[2, 3, 5, 7]
[2, 3, 5, 7, 11, 13, 17, 19]
[2, 3, 5, 7, 11, 13, 17]
[]
[]
``` 

This indicates that the function `count_up_to` is correctly implemented and produces the expected results.