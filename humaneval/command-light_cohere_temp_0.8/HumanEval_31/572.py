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

The function checks if a number is prime by performing basic mathematical tests. It efficiently identifies prime numbers while efficiently avoiding unnecessary calculations. 

This function can be used to quickly determine whether a given number is prime or not, which is very helpful for large datasets or situations where prime checking is needed.