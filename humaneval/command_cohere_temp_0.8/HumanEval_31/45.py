Here's a Python script with a self-contained function that solves the problem:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function defines a logical workflow to determine whether a given number n is prime. It first handles the edge case of n being less than 2, returning False since prime numbers always exceed 1. The function then starts a loop from 2 and iterates up to the square root of n. If n is divisible by any integer within this range, the function returns False, indicating that n is not prime. However, if n hasn't shown any divisibility after this exhaustive search, the function finally returns True, signifying that n is indeed a prime number. 

This algorithm maximizes efficiency by only requiring the square root of n+1 iterations, slightly exceeding the ˜(n/2)  needed in the worst case.