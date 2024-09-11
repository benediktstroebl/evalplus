```python
def fibfib(n: int):
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
        n (int): The position of the number in the sequence.
    
    Returns:
        int: The n-th element of the FibFib number sequence.
    """
    memo = {0: 0, 1: 0, 2: 1}  # Dictionary to store the results of fibfib calls

    def fibfib_helper(k: int):
        # Base cases
        if k in memo:
            return memo[k]
        
        # If not in memo, calculate and store the result
        result = fibfib_helper(k - 1) + fibfib_helper(k - 2) + fibfib_helper(k - 3)
        memo[k] = result  # Store the result in memo
        return result

    return fibfib_helper(n)
```

Here's a breakdown of the solution:

1.  We use a dictionary called `memo` to store the results of previous `fibfib` calls. This is an optimization technique called memoization.
2.  The `fibfib_helper` function is a recursive function that calculates the k-th element of the sequence. It checks if the result is already in `memo`, and if it is, returns the stored result.
3.  If the result is not in `memo`, it calculates the result by calling `fibfib_helper` with `k-1`, `k-2`, and `k-3`, and stores the result in `memo`.
4.  The `fibfib` function simply calls `fibfib_helper` with the input `n` and returns the result.

The time complexity of this solution is O(n), and the space complexity is O(n) as well, due to the use of the `memo` dictionary.

You can test the function with the provided examples:

```python
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```