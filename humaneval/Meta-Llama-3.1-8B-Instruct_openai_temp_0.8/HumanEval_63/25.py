```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibbonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    This function efficiently computes the n-th element of the fibfib number sequence using memoization.
    
    Args:
    n (int): The index of the element in the fibfib sequence.
    
    Returns:
    int: The n-th element of the fibfib sequence.
    """
    # Create a dictionary to store computed values
    memo = {0: 0, 1: 0, 2: 1}
    
    def fibfib_recursive(k: int) -> int:
        # If the value is already computed, return it from the memo
        if k in memo:
            return memo[k]
        
        # Compute the value and store it in the memo
        memo[k] = fibfib_recursive(k-1) + fibfib_recursive(k-2) + fibfib_recursive(k-3)
        return memo[k]
    
    # Call the recursive function to compute the n-th element
    return fibfib_recursive(n)


# Test the function
if __name__ == "__main__":
    print(fibfib(1))  # Expected output: 0
    print(fibfib(5))  # Expected output: 4
    print(fibfib(8))  # Expected output: 24
```

This script defines a function `fibfib` that uses memoization to efficiently compute the n-th element of the fibfib sequence. The function `fibfib_recursive` is a recursive helper function that computes the value and stores it in the memo dictionary. The `if __name__ == "__main__":` block contains test cases to verify the correctness of the function.