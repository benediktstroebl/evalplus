```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function is designed to determine whether a given number is prime. It begins by checking if the number is less than 2, returning False if so, as numbers less than 2 are not prime. The function then iterates through numbers from 2 to the square root of the given number, checking whether the given number is divisible by any of them. If the number is divisible by any, it returns False, indicating that the number is not prime. However, if the loop doesn't find any divisors, it returns True, signifying that the given number is indeed prime.

This function is straightforward and efficient, allowing for a quick evaluation of whether a number is prime or not. It passes the provided tests as it outputs True for prime numbers and False for non-prime numbers, correctly identifying numbers like 6, 4, 1, 13441, 61, and 101 as either prime or not.