```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
        return False
    return True

# Test the function with given markdown code block
is_prime(6) # Should return False
is_prime(101) # Should return True
is_prime(11) # Should return True
is_prime(13441) # Should return True
is_prime(61) # Should return True
is_prime(4) # Should return False
is_prime(1) # Should return False
``` 

This function, `is_prime(n)`, checks if a given number is prime or not using the Sieve of Eratosthenes algorithm. It also passes the