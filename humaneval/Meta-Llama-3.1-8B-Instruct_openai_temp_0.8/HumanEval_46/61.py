### Efficiently Computing the Fib4 Number Sequence
#### Problem Statement
The Fib4 number sequence is defined as follows:
- `fib4(0)` -> 0
- `fib4(1)` -> 0
- `fib4(2)` -> 2
- `fib4(3)` -> 0
- `fib4(n)` -> `fib4(n-1)` + `fib4(n-2)` + `fib4(n-3)` + `fib4(n-4)`

#### Solution
We can efficiently compute the n-th element of the Fib4 number sequence using dynamic programming with memoization.

```python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibbonacci sequence 
    that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    Args:
    n (int): The position of the element in the Fib4 number sequence.

    Returns:
    int: The n-th element of the Fib4 number sequence.
    """
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    
    # Initialize the memoization dictionary
    memo = {0: 0, 1: 0, 2: 2, 3: 0}
    
    # Compute the n-th element using dynamic programming
    for i in range(4, n + 1):
        memo[i] = memo[i-1] + memo[i-2] + memo[i-3] + memo[i-4]
    
    return memo[n]
```

#### Example Usage
```python
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This solution uses a memoization dictionary to store the previously computed elements of the Fib4 number sequence, which significantly improves the efficiency of the computation.