```python
def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
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

Let's break down the code step by step:
1. `is_prime` function: This function is used to determine whether a given number is a prime number or not. It's an essential tool for solving this problem.
2. `count_up_to` function: This function solves the original problem. It uses the `is_prime` function to generate a list of prime numbers less than or equal to `n` and returns the first `n` numbers of this list.

The `count_up_to` function iterates through numbers from 2 up to `n`. It maintains a count of prime numbers found and appends them to the `primes` list. Once the count reaches `n`, the function returns the `primes` list, which contains the desired prime numbers.

Using functions like `is_prime` helps to solve problems like this one in a more efficient and organized manner, especially when dealing with more complex scenarios.