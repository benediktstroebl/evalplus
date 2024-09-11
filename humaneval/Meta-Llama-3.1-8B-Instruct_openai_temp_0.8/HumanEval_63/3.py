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
        n (int): The position of the element in the sequence.

    Returns:
        int: The nth element of the FibFib number sequence.
    """
    
    # Base cases
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1

    # Initialize a list to store the Fibonacci numbers
    fibfib_numbers = [0, 0, 1]
    
    # Compute the Fibonacci numbers from 3 to n
    for i in range(3, n + 1):
        # The ith number is the sum of the (i-1)th, (i-2)th, and (i-3)th numbers
        fibfib_numbers.append(fibfib_numbers[i-1] + fibfib_numbers[i-2] + fibfib_numbers[i-3])
    
    # Return the nth number
    return fibfib_numbers[n]


# Test cases
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This script defines a function `fibfib` to compute the nth element of the FibFib number sequence. It first handles the base cases, then initializes a list `fibfib_numbers` to store the Fibonacci numbers. It computes the Fibonacci numbers from 3 to n and returns the nth number. The test cases at the end verify the correctness of the function.