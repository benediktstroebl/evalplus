Here's a Python script with a self-contained function that solves the x_or_y problem and passes the tests provided in the markdown code block:
```python
def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def x_or_y(n, x, y):
    """Return x if n is prime, else return y."""
    if is_prime(n):
        return x
    else:
        return y

# Examples:
# x_or_y(7, 34, 12) == 34
# x_or_y(15, 8, 5) == 5
```

Let's break down the code:
- The `is_prime` function is used to determine whether a given number n is prime or not. It's a simple primality test that checks if n is less than 2 (thus not prime) or if there exists an integer i between 2 and the square root of n (inclusive) such that n is divisible by i. If either of these conditions is met, it returns False, otherwise, it returns True. 
- The `x_or_y` function takes in three arguments: n (the input number), x (the value to be returned if n is prime), and y (the value to be returned if n is not prime). It uses the `is_prime` function to determine whether n is prime or not. If n is prime, it returns x, otherwise it returns y. 
- The last two lines are examples that demonstrate the behavior of the `x_or_y` function.

This code will give the correct answer (x) for prime inputs (n) and the correct answer (y) for non-prime inputs (n).