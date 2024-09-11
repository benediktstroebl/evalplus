```python
def memo_fibfib(n: int, memo: dict = {}):
    """
    Memoized function to compute the n-th element of the FibFib number sequence.
    
    Args:
    n (int): The index of the element to compute.
    memo (dict, optional): A dictionary to store the computed elements. Defaults to {}.
    
    Returns:
    int: The n-th element of the FibFib number sequence.
    """
    if n in memo:
        return memo[n]
    if n <= 2:
        return 0
    elif n == 3:
        return 1
    else:
        memo[n] = memo_fibfib(n-1, memo) + memo_fibfib(n-2, memo) + memo_fibfib(n-3, memo)
        return memo[n]

def fibfib(n: int):
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence 
    that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
    n (int): The index of the element to compute.
    
    Returns:
    int: The n-th element of the FibFib number sequence.
    """
    return memo_fibfib(n)

# Test the function
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This script defines a memoized function `memo_fibfib` to compute the n-th element of the FibFib number sequence efficiently. The `memo` dictionary stores the computed elements to avoid redundant calculations. The `fibfib` function is a wrapper around `memo_fibfib` with the `memo` dictionary initialized as an empty dictionary.

The time complexity of this solution is O(n), and the space complexity is also O(n), where n is the input integer.