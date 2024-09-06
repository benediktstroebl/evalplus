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

# Unit tests
tests = [
    (7, 34, 12, 34),
    (15, 8, 5, 5),
    (2, 42, 13, 13),
    (25, 74, 18, 18),
    (157, 233, 451, 451),
    (104, 528, 344, 344)
]

for n, x, y, expected in tests:
    result = x_or_y(n, x, y)
    if result != expected:
        print(f"For inputs {n}, {x} and {y}, expected {expected} but got {result}")
``` 

This script defines a function `x_or_y` that takes three arguments (`n`, `x`, and `y`) and returns `x` if the former is a prime number and `y` otherwise. 

The `is_prime` function is used to test if a number is prime. It handles the special cases of numbers less than or equal to 1 being non-prime and numbers less than or equal to 3 being prime. It then performs a iterative precheck on the numbers to determine if they are prime or not. 

The script also includes a list of test cases with corresponding expected outputs. The `x_or_y` function is called for each test case, and the actual output is compared to the expected output. If they don't match, an error message is printed. 

This self-contained script can be executed independently to test out the `x_or_y` function and its unit tests.  It is recommended to run it in a Python environment to get output in the console and inspect the tests.  You can also copy the content of the code block and run it in an IDE or any Python environment.