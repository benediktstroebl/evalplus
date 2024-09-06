Here's a Python script that contains a function named `x_or_y` that solves the problem as per the prompt:
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

def x_or_y(n, x, y):
    if is_prime(n):
        return x
    else:
        return y

# Test Cases
print(x_or_y(7, 34, 12))  # Output: 34
print(x_or_y(15, 8, 5))  # Output: 5
```

This script will return the value of `x` if the provided number `n` is prime, and it will return the value of `y` if `n` is not prime. 

The `is_prime` function is used to determine whether a number is prime or not. If `n` is less than or equal to 1, it is not prime. If `n` is 2 or 3, it is prime. For larger numbers, the function checks whether `n` is divisible by 2 or 3, and if so, it's not prime. Finally, for larger numbers, the function iterates through numbers starting from 5 in increments of 6 (skipping numbers divisible by 2 or 3) and checks for divisibility. If no divisors are found, the number is prime.