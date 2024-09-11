```python
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence 
    that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    This function efficiently computes the n-th element of the fibfib number sequence.
    
    :param n: The position of the FibFib number to compute.
    :return: The n-th element of the FibFib number sequence.
    """
    if n < 2:
        return 0
    elif n == 2:
        return 1
    elif n == 3:
        return 1
    else:
        # Initialize a list to store the last three FibFib numbers
        fibfib_numbers = [0, 0, 1]
        
        # Compute the first 3 numbers
        for _ in range(3, n + 1):
            # The next number is the sum of the last three numbers
            next_fibfib = fibfib_numbers[1] + fibfib_numbers[2] + fibfib_numbers[0]
            # Move the numbers one position to the right
            fibfib_numbers[0] = fibfib_numbers[1]
            fibfib_numbers[1] = fibfib_numbers[2]
            fibfib_numbers[2] = next_fibfib
        
        # The n-th FibFib number is the last number in the list
        return fibfib_numbers[2]


# Test the function
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```

This script defines the `fibfib` function to compute the n-th element of the FibFib number sequence. It uses a list to store the last three numbers in the sequence, which are used to compute the next number in the sequence. The function handles the base cases where n is 0, 1, 2, or 3 explicitly, and uses a loop to compute the fibfib numbers for n greater than 3. The test cases at the end of the script demonstrate the function's correctness.