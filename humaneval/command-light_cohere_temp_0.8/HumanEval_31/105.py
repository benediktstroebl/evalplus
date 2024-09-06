Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
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
This function, `is_prime`, takes an integer `n` as input and checks whether it is prime. 

The function initially handles special cases: `n <= 1` returns `False`, and `n <= 3` returns `True`. 

Then, the function starts a loop and repeatedly checks divisibility by squares up to the square root of `n`, using `i * i <= n`. It returns `True` if no divisors are found, indicating the number is prime;  Otherwise, it returns `False`. 

This function can efficiently determine whether a given number is prime or not, which is a fundamental concept in number theory.