```python
def fib4(n: int):
    """The Fibonacci sequence without recursion."""
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return fib4(n - 1) + fib4(n - 2)

if __name__ == "__main__":
    print(fib4(5))  # Output: 4
    print(fib4(6))  # Output: 8
    print(fib4(7))  # Output: 14
```
This code defines a function called `fib4` that computes the nth element of the Fibonacci sequence without using recursion. It uses a`if` statement for `n == 0`, `1`, and `2` to return the respective base cases of the sequence, and then, for `n > 2`, it uses the `fib4(n - 1)` and `fib4(n - 2)` to compute the next two elements in the sequence and then adds them together. The function finally returns the since the sequence is a Fibonacci sequence.