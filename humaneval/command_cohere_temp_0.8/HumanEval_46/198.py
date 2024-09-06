```python
def fib4(n: int) -> int:
    """
    The Fib4 number sequence is a sequence similar to the Fibbonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    ```
    Length of the Fib4 sequence is 4^N, so we compute the sequence incrementally in a loop
    Returns:
        int: The n-th element of the Fib4 number sequence.
    """
    max_val = 2 ** (n - 1)
    seq = [0] * 4
    curr = 0
    for i in range(2, n + 1):
        new_val = seq[i - 1] + seq[i - 2] + seq[i - 3] + seq[i - 4]
        seq.append(new_val)
        curr += 1
        if curr == max_val:
            curr = 0
            max_val *= 4
    return seq[n]
```

This script defines a `fib4` function that calculates the n-th element of the Fib4 sequence efficiently without using recursion. It uses an iterative approach to calculate the sequence incrementally and terminates when the maximum value of the sequence is reached. The final `seq` list contains the first `n+1` elements of the Fib4 sequence, and `seq[n]` is the n-th element of the sequence, which is returned as a result.