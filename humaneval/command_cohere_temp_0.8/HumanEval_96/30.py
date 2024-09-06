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

This script defines two functions: `is_prime`, which checks if a given number is prime, and `count_up_to`, which returns the first `n` prime numbers less than `n` from the prime number list. 

To do this, the `count_up_to` function iterates through all numbers between 2 and `n`, and for each number, it checks if it's prime using the `is_prime` function. If the number is prime and less than `n`, it adds it to the `prime_list` and increments the count. Once the count reaches `n`, it breaks out of the loop to stop collecting primes.

This solution is efficient and can quickly find primes since more sophisticated algorithms are not necessary for this problem and its constraints.