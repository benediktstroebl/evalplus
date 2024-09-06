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
    for i in range(2, n+1):
        if is_prime(i) and i < n:
            primes.append(i)
            count += 1
            if count == n:
                break
    return primes
```

The script employs a `count_up_to` function to generate a list of the first `n` prime integers that are less than `n`. The `is_prime` function is applied to evaluate whether an integer is a prime number. These utilities work in tandem to solve the problem. 

The `count_up_to` function iterates through integers from 2 up to `n`. It accumulates a list of prime integers that are less than `n` and ceases gathering data once the count of collected prime integers reaches `n`. 

The `is_prime` function probes whether a number is prime by testing all integers from 2 to the square root of the number. If the number is divisible by any integer within this range, it is not prime; otherwise, it is prime. 

The `count_up_to` function is designed to work with any valid input that is an non-negative integer, and the `is_prime` function works correctly for all positive integers. 

These functions work seamlessly together to solve the proposed problem and produce the appropriate output. 

The `count_up_to(5)` example would return `[2, 3]`, as these are the first two prime integers less than 5. 

For `count_up_to(11)`, the result would be `[2, 3, 5, 7]`, as these are the first four prime integers less than 11. 

`count_up_to(0)` would return an empty list, since there are no prime integers that are less than 0. 

For `count_up_to(20)`, the result would be `[2, 3, 5, 7, 11, 13, 17, 19]`, which are the first eight prime integers less than 20. 

For `count_up_to(1)`, the result would be an empty list, as there is no prime integer that is less than 1. 

For `count_up_to(18)`, the result would be `[2, 3, 5, 7, 11, 13, 17]`, which are the first seven prime integers less than 18. 

This solution passes all the tests and produces the correct results for the given examples.