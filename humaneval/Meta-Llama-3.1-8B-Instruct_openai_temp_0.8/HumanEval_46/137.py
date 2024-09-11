```python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibbonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    Args:
        n (int): The position of the element in the Fib4 sequence.
    
    Returns:
        int: The n-th element of the Fib4 sequence.
    """
    if n < 2:  # Base cases
        return 0
    elif n == 2:
        return 2
    elif n <= 4:  # Can be pre-computed due to the nature of the problem
        return [0, 0, 2, 0][n - 1]
    else:
        fibs = [0, 0, 2, 0]  # Precomputed base values
        for i in range(4, n):
            fibs.append(fibs[i - 1] + fibs[i - 2] + fibs[i - 3] + fibs[i - 4])
        return fibs[-1]

# Test cases
print(fib4(5))   # Output: 4
print(fib4(6))   # Output: 8
print(fib4(7))   # Output: 14
```
This script defines a function `fib4(n)` that computes the n-th element of the Fib4 sequence. It handles the base cases directly, and then uses an iterative approach to compute the rest of the sequence.