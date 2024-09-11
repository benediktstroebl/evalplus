```python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibbonacci sequence 
    that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    This function efficiently computes the n-th element of the fib4 number sequence 
    using dynamic programming.

    Args:
        n (int): The index of the fib4 number to compute.

    Returns:
        int: The n-th element of the fib4 number sequence.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    # Initialize a list to store the fib4 numbers, 
    # with the first four elements already computed
    fib4_list = [0, 0, 2, 0]
    
    # Compute the fib4 numbers up to the n-th element
    for i in range(4, n + 1):
        next_fib4 = fib4_list[i - 1] + fib4_list[i - 2] + fib4_list[i - 3] + fib4_list[i - 4]
        fib4_list.append(next_fib4)
    
    # Return the n-th fib4 number
    return fib4_list[n]

# Test the function
print(fib4(5))  # 4
print(fib4(6))  # 8
print(fib4(7))  # 14
```

This script defines a function `fib4(n)` that computes the n-th element of the fib4 number sequence using dynamic programming. It initializes a list `fib4_list` with the first four elements of the sequence and then iteratively computes the next elements up to the n-th element. The function finally returns the n-th element of the sequence.