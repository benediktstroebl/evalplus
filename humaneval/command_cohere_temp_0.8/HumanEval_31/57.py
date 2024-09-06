Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function defines a logical and efficient algorithm to determine whether a given number n is prime. It begins by checking if n is less than 2, returning False if so, as numbers less than 2 are not prime. The function then iterates from 2 up to the square root of n. If n is divisible by any integer within this range, the function returns False, indicating that n is not prime. This iteration process efficiently rules out divisors up to the square root, optimizing the algorithm. However, if n remains undivisible throughout this process, the function returns True, indicating that n is indeed a prime number. This algorithm's efficiency is demonstrated by the fact that it correctly identifies prime numbers while only requiring a linear time complexity of O(√n).