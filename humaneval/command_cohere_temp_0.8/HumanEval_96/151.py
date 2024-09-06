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

The `count_up_to()` function loops through integers from 2 up to `n`, it checks each integer with the `is_prime()` function. If it's a prime number and less than `n`, it's added to the `primes` list. The `count` variable keeps track of how many primes have been found. Once `count` reaches `n`, the function stops looping and returns the list of primes.

To verify that the function works, we can do some spot checks like `count_up_to(5) => [2,3]` and `count_up_to(20) => [2,3,5,7,11,13,17,19]`. These should all return the correct prime numbers and meet the conditions laid out in the task description. 

You can test this script further by calling `count_up_to()` with a variety of inputs to ensure it passes the various edge cases like `count_up_to(0) => []`, `count_up_to(1) => []`, and `count_up_to(18) => [2,3,5,7,11,13,17]`. 

Let me know if you would like to evaluate this script with more extensive tests or discuss any particular aspect of the solution.