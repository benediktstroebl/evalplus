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
The function uses a simple algorithm to determine whether a given number is prime or not. The function starts by handling special cases where the number is less than or equal to 1, as these are clearly not prime. It then checks for divisibility by 2 and 3, as these are the only even prime numbers less than 6. The function then enters a "loop" phase, where it starts with i = 5 and continuously raises i by adding 6 each time, while checking for divisibility with the current value of n and its double. The loop continues until the maximum number in the range that hasn't been reached yet, at which point, n should be a prime number.