Here's a Python script with a self-contained function that solves the problem and passes the tests:
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

# Test cases
n1 = 7
x1 = 34
y1 = 12
print(f"{x_or_y(n1, x1, y1)} == {x1}")

n2 = 15
x2 = 8
y2 = 5
print(f"{x_or_y(n2, x2, y2)} == {y2}")
```

This script includes a `is_prime` function that tests if a given number is prime. The `x_or_y` function uses this to decide whether to return `x` or `y`. The test cases are also included, and the script will run to print the results of these tests. 

The `is_prime` function is a basic optimized implementation that checks for divisibility up to the square root of the number. A number is considered prime if it is greater than 1 and has no divisors other than 1 and itself. 

The `x_or_y` function utilizes the `is_prime` function to determine whether n is prime. If it is, the function returns x, otherwise, it returns y. This functionality is exemplified in the test cases included in the script, where the correct values are returned based on the primality of the number.