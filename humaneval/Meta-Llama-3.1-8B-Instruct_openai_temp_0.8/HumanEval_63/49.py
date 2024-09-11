```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
    n (int): The position of the element in the FibFib sequence to be computed.
    
    Returns:
    int: The n-th element of the FibFib sequence.
    
    Raises:
    ValueError: If n is not a non-negative integer.
    """
    
    # Check if n is a non-negative integer
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")
    
    if n == 0 or n == 1:
        # Base case: fibfib(0) == 0, fibfib(1) == 0
        return 0
    elif n == 2:
        # Base case: fibfib(2) == 1
        return 1
    else:
        # Initialize a list to store the first three elements of the sequence
        fibfib_sequence = [0, 0, 1]
        
        # Compute the next elements of the sequence
        for i in range(3, n + 1):
            # The next element is the sum of the previous three elements
            next_element = fibfib_sequence[i - 1] + fibfib_sequence[i - 2] + fibfib_sequence[i - 3]
            # Append the next element to the sequence
            fibfib_sequence.append(next_element)
        
        # Return the n-th element of the sequence
        return fibfib_sequence[n]


# Test the function
if __name__ == "__main__":
    import doctest
    doctest.testmod()
```
This Python script defines a function `fibfib` that computes the n-th element of the FibFib sequence. The function first checks if the input `n` is a non-negative integer. If not, it raises a `ValueError`. Otherwise, it uses dynamic programming to compute the first `n` elements of the sequence and returns the n-th element. The script also includes a test for the function using the `doctest` module.