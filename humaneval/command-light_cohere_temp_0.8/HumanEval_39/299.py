Here's the solution for the provided markdown code block:

```python
def prime_fib(n: int) -> int:
    if n <= 1:
        return n
    elif n <= 3:
        return 3
    elif n % 2 == 0:
        return 5
    else:
        a, b = 6, 5
        for _ in range(n // 2):
            a, b = b, a + b
        if a > 1:
            return a
        elif b > 1:
            return b
    else:
        raise ValueError("n should be greater than 4 to produce a Fibonacci number and prime")
```
This Python function uses an if-else structure to check for the n-th Fibonacci number and whether it's prime. The function then returns the numbers in the Fibonacci sequence that are prime when n is greater than 4.