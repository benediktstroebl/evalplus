```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n == 2:
        return 2
    elif n % 2 == 0:
        return 3
    else:
        a, b = 2, 3
        while a < n:
            if b >= n:
                break
            c = a
            a = b
            b = c + 1
        return b

# Driver code to test the function
def test_prime_fib():
    print("First few prime Fibonacci numbers:")
    for _ in range(5):
        print(prime_fib(_))

test_prime_fib()
```
The code defines a function called `prime_fib` that calculates the n-th prime Fibonacci number and returns it. It uses an algorithm that trial and error by testing values for `a` and `b` to find the next Fibonacci number while ensuring `b` is greater than or equal to `a` to avoid overflow. The code also provides a tests the function with the `test_prime_fib` function.