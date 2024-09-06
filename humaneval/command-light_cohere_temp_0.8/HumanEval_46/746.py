```python
def fib4(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        return fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4)

# Unit tests
test_fib4 = []

test_fib4.add(assert(fib4(5) == 4))
test_fib4.add(assert(fib4(6) == 8))
test_fib4.add(assert(fib4(7) == 14))

# Output:
```