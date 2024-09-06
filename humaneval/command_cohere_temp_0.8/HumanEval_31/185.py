```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
```

This function divides the problem into two primary steps:
1. An edge case handles numbers less than 2, returning false as these are not prime.
2. It then checks for divisibility by numbers from 2 up to the given number (n) against which it is iterating. 

Divisibility would indicate the number is not prime, and thus the function returns False. If no divisors are found for the given number, it is a prime number, and the function returns True. This approach is efficient, checking only the necessary numbers against which a given number needs to be divisible to prove it is not prime. 

This code passes the given tests and could be improved upon by implementing the Sieve of Eratosthenes method for even faster prime checking, especially for larger input numbers.