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

The `count_up_to()` function iterates through numbers from 2 up to `n`, it checks each number using the `is_prime()` function to verify if it's a prime number and if it's less than `n`. If it is a prime number, it adds it to the `primes` list and increments the `count` counter. Once the counter reaches `n`, it stops iterating and returns the list of prime numbers.

To ensure the correctness of the `is_prime()` function, it checks if the number is less than 2, which is not prime, it returns False. It also checks divisibility by numbers from 2 to the square root of the number, if the number is divisible by any of them, it returns False. If it gets through the loop without finding a divisor, it returns True. 

You can test the functions using `count_up_to(n)`, for example:
```python
print(count_up_to(5)) # [2,3]
print(count_up_to(11)) # [2,3,5,7]
print(count_up_to(20)) # [2,3,5,7,11,13,17,19]
print(count_up_to(100)) # [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
```