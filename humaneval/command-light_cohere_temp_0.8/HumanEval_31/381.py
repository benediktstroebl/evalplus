Here is a Python script that checks whether a given number is a prime number, following the markdown code problem:
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
This function uses a simple algorithm to check for prime numbers. It starts by checking numbers less than or equal to 2 and 3, then moves on to check divisibility by numbers of the form \(i^2\) for \(i = 5\), where \(i\) is increased by 6 each time. The function then returns true if no divisors were found after the loop.