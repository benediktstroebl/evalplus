```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones. The Fibonacci sequence starts with 0 and 1, and the sequence continues with each addition of new numbers.
    return:
        if n < 0:
            raise ValueError("n must be a non-negative integer.")
        if n == 0:
            return 0
        if n == 1:
            return 1
        prev = 1
        curr = 1
        for _ in range(2, n):
            next_num = prev + curr
            prev, curr = curr, next_num
        return curr
```