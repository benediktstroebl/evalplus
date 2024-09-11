```python
def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibonacci sequence 
    that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
        n (int): The index of the number in the sequence.
    
    Returns:
        int: The n-th number in the FibFib number sequence.
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    elif n <= 3:
        return 1
    else:
        memo = [0, 0, 1, 1]
        
        for i in range(4, n + 1):
            memo.append(memo[i - 1] + memo[i - 2] + memo[i - 3])
        
        return memo[n]

# Test cases
print(fibfib(1))    # Expected output: 0
print(fibfib(5))    # Expected output: 4
print(fibfib(8))    # Expected output: 24
```
To use the `fibfib` function, simply call it with an integer argument representing the index of the number in the sequence. The function will return the corresponding number in the FibFib sequence. Note that the time complexity of this function is O(n) due to the use of dynamic programming for memoization. This is more efficient than the naive recursive approach, which would have a time complexity of O(3^n) due to repeated computation.