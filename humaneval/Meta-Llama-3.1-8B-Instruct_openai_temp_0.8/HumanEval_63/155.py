```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence 
    that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
    n (int): The position of the number in the FibFib sequence.
    
    Returns:
    int: The n-th number in the FibFib sequence.
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        # We use an array to store the previously computed values
        fibfib_values = [0] * (n + 1)
        fibfib_values[0] = 0
        fibfib_values[1] = 0
        fibfib_values[2] = 1
        
        # We compute the fibfib values for n = 3 to n
        for i in range(3, n + 1):
            # We use the recurrence relation to compute the fibfib value
            fibfib_values[i] = fibfib_values[i-1] + fibfib_values[i-2] + fibfib_values[i-3]
        
        # We return the n-th fibfib value
        return fibfib_values[n]

# Test the function
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This script defines a function called `fibfib(n)` that calculates the n-th number in the FibFib sequence. The function takes an integer `n` as input and returns the corresponding FibFib number.
The function first checks the base cases for n <= 1 and n == 2. For n > 2, it uses a dynamic programming approach to compute the FibFib values.
The function creates an array `fibfib_values` to store the previously computed values and initializes the base cases. It then computes the FibFib values for n = 3 to n using the recurrence relation, and finally returns the n-th FibFib value.

The script also includes some test cases to verify the correctness of the function.