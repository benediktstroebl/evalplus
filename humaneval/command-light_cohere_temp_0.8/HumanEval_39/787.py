```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return prime_fib(n // 2) + 2
    return prime_fib(n // 2) + (n % 2) + 2

def test_prime_fib():
    print("Test 1:", prime_fib(1))
    print("Test 2:", prime_fib(2))
    print("Test 3:", prime_fib(3))
    print("Test 4:", prime_fib(4))
    print("Test 5:", prime_fib(5))
    print("Test 6:", prime_fib(6))
    print("Test 7:", prime_fib(7))
    print("Test 8:", prime_fib(8))
    print("Test 9:", prime_fib(9))
    print("Test 10:", prime_fib(10))

# Run the function test_prime_fib() to see the test output
```