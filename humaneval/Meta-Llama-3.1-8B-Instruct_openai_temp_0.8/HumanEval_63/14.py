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
        n (int): The position of the number in the sequence.

    Returns:
        int: The nth number in the sequence.

    Raises:
        ValueError: If n is less than 0.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    # Base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1

    # Initialize a list to store the sequence
    fibfib_seq = [0, 0, 1] + [0]*(n-2)

    # Compute the sequence
    for i in range(3, n+1):
        fibfib_seq[i] = fibfib_seq[i-1] + fibfib_seq[i-2] + fibfib_seq[i-3]

    return fibfib_seq[n]

# Test the function
print(fibfib(1)) # Expected output: 0
print(fibfib(5)) # Expected output: 4
print(fibfib(8)) # Expected output: 24
```

However, a more efficient approach is to use dynamic programming to store the already computed values to avoid redundant calculations. Here's a revised version of the script:

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
        n (int): The position of the number in the sequence.

    Returns:
        int: The nth number in the sequence.

    Raises:
        ValueError: If n is less than 0.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    # Base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1

    # Initialize a dictionary to store the sequence
    fibfib_dict = {0: 0, 1: 0, 2: 1}

    # Compute the sequence
    for i in range(3, n+1):
        fibfib_dict[i] = fibfib_dict[i-1] + fibfib_dict[i-2] + fibfib_dict[i-3]

    return fibfib_dict[n]

# Test the function
print(fibfib(1)) # Expected output: 0
print(fibfib(5)) # Expected output: 4
print(fibfib(8)) # Expected output: 24
```

This revised version has a time complexity of O(n) and a space complexity of O(n) because it only stores the already computed values in the dictionary.