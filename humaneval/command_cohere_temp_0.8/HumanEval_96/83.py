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
    prime_list = []
    for num in range(2, n+1):
        if is_prime(num) and num < n:
            prime_list.append(num)
            count += 1
            if count == n:
                break
    return prime_list
```

This script defines two functions: `is_prime`, which checks if a given number is prime, and `count_up_to`, which returns the first `n` prime numbers less than `n` from the list of integers. 

To do so, the `count_up_to` function iterates through the range from 2 to `n`, tracking the count of prime numbers found. When the count reaches `n`, the function stops iterating and returns the list of prime numbers encountered. 

This solution passes all the tests provided in the prompt and should correctly solve the problem.