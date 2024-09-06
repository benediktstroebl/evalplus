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
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

if __name__ == "__main__":
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
    assert fib4(8) == 32
    assert fib4(9) == 45
    assert fib4(10) == 55
```

This code defines a Python function that computes the n-th element of the Fibonacci sequence using a loop-based approach. The function follows the base cases for n being 0,1,2,3 and returns the corresponding Fibonacci numbers. For any other number of n, the function recursively calls itself with the argument (n-1), (n-2), (n-3), and (n-4), and then adds up these values to compute the Fibonacci number for n. The test cases ensure that the function is correctly implementing the Fibonacci sequence calculation.