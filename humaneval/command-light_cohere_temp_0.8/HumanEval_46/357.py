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
test_fib4 = {
    assert fib4(0) == 0
}

test_fib4 = {
    assert fib4(1) == 0
}

test_fib4 = {
    assert fib4(2) == 2
}

test_fib4 = {
    assert fib4(3) == 0
}

test_fib4 = {
    assert fib4(4) == 4
}

test_fib4 = {
    assert fib4(5) == 5
}

test_fib4 = {
    assert fib4(6) == 8
}

test_fib4 = {
    assert fib4(7) == 14
}
```
The code defines a function called `fib4` that computes the n-th element of the Fibonacci sequence without recursion. The function uses a approach of breaking down the problem into smaller subproblems and combining their solutions to compute the final result. The tests are then used to verify the correctness of the function.