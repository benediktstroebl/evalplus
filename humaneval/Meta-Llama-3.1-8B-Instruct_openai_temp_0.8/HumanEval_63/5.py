```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    This function efficiently computes the n-th element of the fibfib number sequence using memoization.
    
    Parameters:
    n (int): The index of the element to be computed in the fibfib sequence.
    
    Returns:
    int: The n-th element of the fibfib sequence.
    """
    # Create a dictionary to store the computed values for memoization
    memo = {0: 0, 1: 0, 2: 1}
    
    # Function to recursively compute the value for a given index
    def fibfib_recursive(i: int) -> int:
        if i in memo:
            # If the value is already in the memo, return it
            return memo[i]
        else:
            # If not, compute the value and store it in the memo
            result = fibfib_recursive(i-1) + fibfib_recursive(i-2) + fibfib_recursive(i-3)
            memo[i] = result
            return result
    
    # If n is in the memo, return its value directly
    if n in memo:
        return memo[n]
    else:
        # Otherwise, compute the value recursively and return it
        return fibfib_recursive(n)

if __name__ == "__main__":
    print(fibfib(1))   # 0
    print(fibfib(5))   # 4
    print(fibfib(8))   # 24
```

In this script, we use a recursive approach with memoization to efficiently compute the n-th element of the fibfib sequence. The `fibfib_recursive` function is used to recursively compute the value for a given index, and the `memo` dictionary is used to store the computed values for memoization. The main `fibfib` function checks if the value is already in the memo and returns it directly if so, or computes it recursively and stores it in the memo if not.