```python
def fib(n):
    if n <= 0:
        return None  # Base case: negative input
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return b

# Test cases
test_fib = {
    'Test 1': (fib(1), '1') == 1,
    'Test 2': (fib(10), '55') == 55,
    'Test 3': (fib(3), '134') == 34,
    'Test 4': (fib(9), '8') == 21,
    'Test 5': is_(fib(5), '342857134512'),  # Long Fibonacci number
}
```
The function 'fib(n)' calculates the n-th Fibonacci number in this solution. It uses an iterative method to compute the Fibonacci sequence. The test cases are also implemented in the same script to confirm the function's correctness.