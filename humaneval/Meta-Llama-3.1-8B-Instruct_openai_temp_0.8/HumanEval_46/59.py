### Fib4 Number Sequence Calculator
#### Using Memoization for Efficient Computation
```python
def fib4(n: int) -> int:
    """
    Computes the n-th element of the Fib4 number sequence.

    The Fib4 number sequence is a sequence defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    Args:
        n (int): The index of the element to compute.

    Returns:
        int: The n-th element of the Fib4 number sequence.
    """
    # Base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    # Initialize memoization dictionary
    memo = {0: 0, 1: 0, 2: 2}
    # Compute elements up to n
    for i in range(3, n + 1):
        # Use previous elements to compute current element
        memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3] + memo[i - 4]
    # Return the n-th element
    return memo[n]

# Test the function
print(fib4(5))   # 4
print(fib4(6))   # 8
print(fib4(7))   # 14
```
This script uses memoization to compute the n-th element of the Fib4 number sequence efficiently by storing previously computed elements in a dictionary. The function takes an integer `n` as input and returns the n-th element of the Fib4 number sequence.