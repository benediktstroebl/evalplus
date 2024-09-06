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
This function, `is_prime`, takes an integer `n` as input and returns `True` if `n` is a prime number and `False` otherwise. It uses age set of rules to determine whether a number is prime or not, with some basic numbers that are known to be prime. 

The function then passes all the tests with a range of values from 2 to the square root of the input number, and returns `True` if any of the tests fail to pass.

The function uses the `if` statement to evaluate the condition of each test. 

It uses a while loop to check if the square of the number is less than or equal to the input number, and if the condition is met, it returns `False`.