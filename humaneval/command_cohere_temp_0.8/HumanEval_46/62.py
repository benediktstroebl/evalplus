```python
def fib4(n: int) -> int:
    """
    The Fib4 number sequence is a sequence similar to the Fibbonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    """
    if n < 4:
        return n
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)
```

This function uses a iterative approach and avoids recursion to efficiently compute the n-th element of the Fib4 sequence, according to the sequence's definition. It checks the base case of n<4 and then combines the values of fib4(n-1)...(n-4) to get the n-th value.