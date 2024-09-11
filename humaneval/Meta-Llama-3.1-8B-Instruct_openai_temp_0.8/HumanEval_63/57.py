```python
def fibfib(n: int) -> int:
    """
    Compute the n-th element of the FibFib number sequence.
    
    The FibFib number sequence is defined as follows:
    fibfib(0) = 0
    fibfib(1) = 0
    fibfib(2) = 1
    fibfib(n) = fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    This function uses memoization to store and reuse previously computed values, 
    resulting in a time complexity of O(n) instead of O(3^n) without memoization.
    
    Args:
        n (int): The index of the element to compute in the FibFib sequence.
    
    Returns:
        int: The n-th element of the FibFib sequence.
    """
    memo = {0: 0, 1: 0, 2: 1}  # Initialize memo dictionary with base cases

    def fibfib_helper(k: int) -> int:
        """
        Recursive helper function to compute the k-th element of the FibFib sequence.
        
        Args:
            k (int): The index of the element to compute in the FibFib sequence.
        
        Returns:
            int: The k-th element of the FibFib sequence.
        """
        if k in memo:  # If k is already in memo, return the stored value
            return memo[k]
        
        # If k is not in memo, compute the value recursively and store it in memo
        result = fibfib_helper(k-1) + fibfib_helper(k-2) + fibfib_helper(k-3)
        memo[k] = result  # Store the result in memo
        return result

    return fibfib_helper(n)  # Return the n-th element of the FibFib sequence


# Test cases
if __name__ == "__main__":
    print(fibfib(1))  # Output: 0
    print(fibfib(5))  # Output: 4
    print(fibfib(8))  # Output: 24
```

This script defines a function `fibfib(n)` that computes the n-th element of the FibFib number sequence using memoization to store and reuse previously computed values. The function uses a recursive helper function `fibfib_helper(k)` to compute the k-th element of the sequence, and a dictionary `memo` to store the computed values. The script also includes test cases to verify the correctness of the function.