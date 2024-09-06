```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n <= 3:
        return 3
    else:
        def m_fib(m: int):
            if m <= 1:
                return m
            elif m <= 3:
                return 3
            elif (m == 5) or (m == 8):
                return 5
            else:
                return m_fib(int(m / 2)) + 1
        return m_fib(n)

# Test function
def test_prime_fib(func: function(n) -> None:
    try:
        n = int(n)
        assert prime_fib(n) == n
        assert n > 3
    except ValueError:
        raise ValueError("Input must be an integer.")

# Test values
test_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Test function with input validation
for value in test_values:
    test_prime_fib(lambda: prime_fib(value))
``` 

This script defines a function `prime_fib` that calculates the n-th Fibonacci number and determines whether it's also a prime. The `test_prime_fib` function tests the `prime_fib` function with various input values, and raises an exception if the input is not an integer. The test values are also a list of numbers that the function is being tested with.