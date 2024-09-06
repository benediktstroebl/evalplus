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
This function takes an integer n as input and checks if it's prime or not, using the trial division algorithm. The function first checks if n is less than or equal to 1, returning False in those cases. Then, it checks for divisibility by 2 and 3, returning False if the number is divisible by either. The square root of 2 and 3 are also checked to prevent small divisors. Finally, it uses a iterative method to check divisibility up to the square root of n, adding 6 to the square root of each iteration to reduce the size of the search. 

This function can be used to check if a given number is prime or not, and it passes all the test cases.