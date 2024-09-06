```python
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
``` 
This function checks whether the given number is prime or not. It employs some basic heur strategies to determine primality, such as checking divisibility by 2 and 3, as well as trying larger primes up to the square root of the number. The function is self-contained and does not require any external functions or variables to solve the problem. 

I hope this function meets the requirement of a self-contained function that solves the prime number checking problem.