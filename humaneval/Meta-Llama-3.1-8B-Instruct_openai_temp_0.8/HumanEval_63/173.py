```python
def fibfib(n: int):
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence, 
    defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
    
    This function efficiently computes the n-th element of the FibFib number sequence.
    
    Args:
        n (int): The position of the number in the sequence.
    
    Returns:
        int: The n-th element of the FibFib number sequence.
    """
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    # Initialize a list to store the Fibonacci-like numbers
    fibfib_nums = [0, 0, 1]
    
    # Compute the FibFib numbers up to the n-th number
    for i in range(3, n + 1):
        # Compute the next number as the sum of the previous three numbers
        next_num = fibfib_nums[i-1] + fibfib_nums[i-2] + fibfib_nums[i-3]
        fibfib_nums.append(next_num)
    
    # Return the n-th number
    return fibfib_nums[n]

# Test cases
print(fibfib(1))  # Expected output: 0
print(fibfib(5))  # Expected output: 4
print(fibfib(8))  # Expected output: 24
```

This script defines a function `fibfib(n)` that efficiently computes the n-th element of the FibFib number sequence. It uses a bottom-up dynamic programming approach to compute the sequence up to the n-th number, and then returns the n-th number. The script also includes test cases to verify the correctness of the function.