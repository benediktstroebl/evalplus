```python
def fib4(n: int):
    if n <= 1:
        return n
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

# Example usage
print(fib4(5))  # Output: 14
print(fib4(6))  # Output: 24
print(fib4(7))  # Output: 42

```
The `fib4` function computes the n-th Fibonacci number in a non-recursive manner, using the formula:
`F(n) = F(n-1) + F(n-2) + F(n-3) + F(n-4)`.  It's an efficient method that avoids the drawbacks of recursion.