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

This Python function is_prime uses a combination of quick testing and loop execution to determine if a number is prime or not. The function first checks if the number is less than or equal to 1, in which case it is definitely not prime. Then, it checks for divisibility by 2 and 3, returning false if either of these numbers are divisors. Next, the function initializes a testing point `i` and increments it by 6 each time, until the square of `i` exceeds the number. This process is testing the for divisibility by numbers just larger than the square of the number being tested.