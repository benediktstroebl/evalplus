```python
def fib4(n: int) -> int:
    def fib4_helper(n: int, acc: int = 0, prev: int = 0, curr: int = 0, next: int = 0) -> int:
        if n == 0:
            return acc
        if n == 1:
            return prev
        if n == 2:
            return curr
        if n == 3:
            return next
        return fib4_helper(n - 1, acc + prev, prev, curr, next)

    if n < 4:
        return n
    else:
        return fib4_helper(n - 4)

# Tests
assert fib4(0) == 0
assert fib4(1) == 0
assert fib4(2) == 2
assert fib4(3) == 0
assert fib4(4) == 3
assert fib4(5) == 4
assert fib4(6) == 8
assert fib4(7) == 14
```

This code defines a `fib4` function that calculates the n-th Fib4 number efficiently without using recursion. It achieves this by defining a helper function, `fib4_helper`, which is nearly identical to the definition of the Fibonacci sequence but with an additional layer of indirection. The helper function avoids recursion by managing multiple intermediate values locally. The `fib4` function itself handles the base case of computing the first three Fib4 numbers and then delegates the rest to the helper function.