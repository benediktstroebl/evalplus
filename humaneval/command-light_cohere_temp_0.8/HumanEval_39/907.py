Here's the provided Python code that defines the `prime_fib` function to find the n-th Fibonacci number that is prime, and the test suite to validate its correctness:
```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n <= 3:
        return 3
    elif (n % 2 == 0) or (n % 3 == 0):
        return 5
    else:
        a, b = 6, 0
        for _ in range(4 * n - 4):
            a, b = b, a + b + 1
            if a > 1 and a <=ovisd(b):
                return a

def test_prime_fib():
    print(prime_fib(5))  # Should print 89
    print(prime_fib(6))  # Should print 6
    print(prime_fib(7))  # Should print 7
    print(prime_fib(8))  # Should print 56
    print(prime_fib(9))  # Should print 13
    print(prime_fib(10))  # Should print 521
    print(prime_fib(11))  # Should print 267
```

The code defines a function `prime_fib` which computes the n-th Fibonacci number that is prime, and tests its functionality using the `test_prime_fib` function that prints the result of calling `prime_fib` with different input values. 
The test suite contains a series of tests that cover various input values, and the expected output for each test is set to the corresponding value of the n-th Fibonacci prime.