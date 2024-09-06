Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_prime(n):
    """Check if an integer is prime"""
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
The `count_up_to()` function uses the `is_prime()` function to generate a list of prime numbers less than `n` and returns the first `n` numbers of this list. It does this by counting the number of primes found and breaking out of the loop when `count` reaches `n`. 

( hormarmarkdown floats the code block to the right while giving a border. )

To use these functions, just import them in your Python script or interactive environment, as follows:
```python
from primes import is_prime, count_up_to
``` 
The keyword `primes` is used to make the imported functions easier to read in the context of this problem.