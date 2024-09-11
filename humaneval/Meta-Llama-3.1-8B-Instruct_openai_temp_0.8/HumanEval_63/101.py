```python
def fibfib(n: int):
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence 
    that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
        n (int): The position of the element in the fibfib sequence.

    Returns:
        int: The nth element of the fibfib sequence.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    elif n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        # Initialize a list to store the fibfib numbers
        fibfib_numbers = [0, 0, 1]
        
        # Compute the fibfib numbers up to the nth element
        for i in range(3, n + 1):
            # Compute the next fibfib number as the sum of the previous three
            next_fibfib = fibfib_numbers[i - 1] + fibfib_numbers[i - 2] + fibfib_numbers[i - 3]
            # Append the next fibfib number to the list
            fibfib_numbers.append(next_fibfib)
        
        # Return the nth fibfib number
        return fibfib_numbers[n]

# Test the function
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This script defines the `fibfib` function to compute the nth element of the fibfib sequence. It uses a list to store the computed fibfib numbers and appends the next number in the sequence as it computes it. The function returns the nth fibfib number. It also includes error checking to ensure the input is a non-negative integer.