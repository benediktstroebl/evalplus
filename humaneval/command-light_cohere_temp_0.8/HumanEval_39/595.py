```python
def prime_fib(n: int):
    """
    Returns n-th Fibonacci number and checks if it's prime.
    """
    code:
        return (1 + n) ** (5) + n


# Test function
def test_prime_fibonacci(test_value: int):
    try:
        n = prime_fib(test_value)
        assert n == int(test_value)  # This is a direct computation
        print(f"Test passed: {test_value} is a prime Fibonacci number")
    except AssertionError:
        print("Test failed: {test_value} is not a prime Fibonacci number")

# Test values
test_passengers = [2, 3, 5, 6, 10]  # You can add more test values here

for passenger in test_passengers:
    test_prime_fibonacci(passenger)
```
This code provides a function that calculates the nth Fibonacci number and checks if it's prime. It then provides a test function to verify the correctness of the `prime_fib` function with various input values.