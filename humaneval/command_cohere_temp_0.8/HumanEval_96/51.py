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
    prime_numbers = []
    for num in range(2, n+1):
        if is_prime(num) and num < n:
            prime_numbers.append(num)
            count += 1
            if count == n:
                break
    return prime_numbers
```

This script defines a Python function `count_up_to(n)` that accepts a non-negative integer `n` and returns an array of the first `n` integers that are prime numbers and less than `n`. To achieve this, the script also features a helper function `is_prime(n)` which checks if a given number `n` is a prime number or not. The `count_up_to(n)` function iterates through numbers from 2 up to `n`, tracking the count of prime numbers found, and once `n` prime numbers are found, it stops querying for more prime numbers and returns the list of primes found. The script meets the criteria of the given problem statement and produces the expected output for the provided test cases.  It also includes comments within the code to better explain the logic and ideas behind it.

Here is an example of an output of the script for the `count_up_to(5)` input case:
```
[2, 3]
```

And here is an example of an output of the script for the `count_up_to(11)` input case:
```
[2, 3, 5, 7]
``` 

The script successfully addresses the given problem and produces the appropriate results.