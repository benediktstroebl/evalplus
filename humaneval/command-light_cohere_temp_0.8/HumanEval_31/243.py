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
This code defines a function is_prime that checks whether a given number n is a prime number or not. The function uses basic primality tests, starting with the assumption that numbers less than or equal to 3 are prime. Then, it checks for divisibility by 2 and 3, returning False if either of these numbers are divisors. If the number fails any these tests, it starts checking for divisibility by smaller prime numbers, ensuring that the square of the next prime number is less than or equal to n. 

The function then returns True if the number is prime and False otherwise.