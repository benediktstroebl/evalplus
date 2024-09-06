Here is a self-contained Python script that defines a function `is_prime()` that checks whether a given number is a prime:

```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
        return False
    return True
```

This function uses a 'backtracking' algorithm to determine whether a number is prime. It iterates through a range of numbers from 2 up, and whenever it finds a number that divides the given number without a remainder, it returns 'False'.  You can also use this function to check if specific numbers are prime by calling it with the desired input number.