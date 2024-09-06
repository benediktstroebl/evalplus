Here's the self-contained Python script that solves the Fibonacci sequence problem without recursion:
```python
def fib4(n: int) -> int:
    """
    Initialize the Fibonacci sequence.
    fib_0 = 0
    fib_1 = 1
    prev = fib_0
    curr = fib_1
    for _ in range(n):
        prev, curr = curr, prev + curr
    return curr
```
This function calculates the nth element in the Fibonacci sequence, where n is the input parameter. It uses a iterative approach to compute the sequence by updating the current and previous values simultaneously. The function returns the `curr` which is the nth Fibonacci number in the sequence.