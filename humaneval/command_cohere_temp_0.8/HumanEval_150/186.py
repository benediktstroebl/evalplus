Here's a Python script with a self-contained function that solves the x_or_y problem and passes the tests:
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

# Example usage
print(x_or_y(7, 34, 12))  # Output: 34
print(x_or_y(15, 8, 5))  # Output: 5
```

This code defines a function `x_or_y` that takes three arguments: an input number `n`, and two values `x` and `y` whose return is dependent on the input number `n`. The function uses the `is_prime` function to determine whether `n` is a prime number or not. If it is prime, the function returns `x`, otherwise, it returns `y`.

The `is_prime` function also checks whether the given number n is less than or equal to 1, in which case it returns False. It also checks for n to be less than or equal to 3, in which case it returns True. If the number is not prime, it checks if n is divisible by 2 or 3, and returns False. If the number is not prime, it uses the algorithm of trial division to check for divisibility by successive primes starting from 5. If the number is not prime, it returns False.

The code also includes example usages of the `x_or_y` function which print the correct output for the given test cases.

Feel free to ask any questions or to proceed with further problems!