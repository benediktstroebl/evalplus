```python
def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
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

This script defines a `count_up_to` function that solves the problem as described in the prompt. It takes an integer `n` as input and returns the first `n` prime numbers less than `n`. 

The `is_prime` function is used to determine if a number is prime. It uses a simple algorithm that checks if the number is less than or equal to 1, it returns `False`; if the number is divisible by any number from 2 to the square root of the number, it returns `False`. If neither of these conditions is met, it returns `True`. 

The `count_up_to` function uses a loop to iterate through integers from 2 up to but not including `n`. For each number, it checks if the number is prime and if it is less than `n`, it adds it to the `prime_numbers` list. The `count` keeps track of the number of prime numbers collected so far. Once `count` reaches `n`, the function breaks out of the loop to stop collecting primes. 

This solution is efficient and can solve the problem for reasonably large values of `n` in a reasonable time. It also has room for improvements if needed.