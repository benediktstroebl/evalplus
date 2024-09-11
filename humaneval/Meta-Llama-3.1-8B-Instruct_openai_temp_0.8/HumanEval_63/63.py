```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
    n (int): The index of the fibfib number to compute.
    
    Returns:
    int: The n-th element of the fibfib number sequence.
    """
    if n == 0:
        # base case: fibfib(0) == 0
        return 0
    elif n == 1:
        # base case: fibfib(1) == 0
        return 0
    elif n == 2:
        # base case: fibfib(2) == 1
        return 1
    else:
        # Initialize a list to store the fibfib numbers
        fibfib_numbers = [0, 0, 1]
        
        # Compute the fibfib numbers up to the n-th number
        for i in range(3, n + 1):
            # Calculate the next fibfib number as the sum of the previous three numbers
            next_number = fibfib_numbers[i - 1] + fibfib_numbers[i - 2] + fibfib_numbers[i - 3]
            # Append the next fibfib number to the list
            fibfib_numbers.append(next_number)
        
        # Return the n-th fibfib number
        return fibfib_numbers[n]

# Test the function
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This script uses dynamic programming to compute the n-th element of the fibfib number sequence. It initializes a list to store the first three fibfib numbers (0, 0, and 1) and then iteratively computes the remaining fibfib numbers up to the n-th number. The n-th fibfib number is then returned. The base cases are handled separately to ensure the function returns the correct results for n = 0, 1, and 2.