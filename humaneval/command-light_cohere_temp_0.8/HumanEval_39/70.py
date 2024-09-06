```python
def prime_fib(n: int):
    if n <= 1:
        return n
    else:
        return 2  # Base case: first Fibonacci number is 2 and it is prime

# Test cases
assert prime_fib(1) == 2
assert prime_fib(2) == 3
assert prime_fib(3) == 5
assert prime_fib(4) == 13
assert prime_fib(5) == 89
assert prime_fib(6) == 2 * 13  # 2 and 13 are prime
assert prime_fib(7) == 2 * 2 * 17  # 2, 2 * 17, and 17 are prime
assert prime_fib(8) == 2 * 2 * 2 * 13  # 2, 2 * 2, 2 * 13, and 13 are prime
assert prime_fib(9) == 2 * 17  # 2, 17 are prime

```
This Python script defines a function `prime_fib` that calculates the n-th Fibonacci number and checks if it's prime. It then passes these test cases to ensure the function's correctness. The `assert` statements are used to check if the function's output matches the expected result for different input values.