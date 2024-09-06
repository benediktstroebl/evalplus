```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
```

This function returns `True` if the given number is prime, and `False` otherwise. It first checks if the given number is less than 2, and since primes are defined to be greater than 1, it returns `False` in such a case. It then starts a loop from 2 and goes up to the given number, checking if the number is divisible by any other number. If it is, then the function returns `False` as it is not a prime number. However, if the number is not divisible by any other number, then it is a prime and the function returns `True`. 

This solution passes the given tests, as the function correctly identifies prime and non-prime numbers according to the problem statement. 
```python
# Test the function
assert is_prime(6) == False
assert is_prime(101) == True
assert is_prime(11) == True
assert is_prime(13441) == True
assert is_prime(61) == True
assert is_prime(4) == False
assert is_prime(1) == False
```