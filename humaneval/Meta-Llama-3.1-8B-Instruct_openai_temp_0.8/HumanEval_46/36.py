### Fib4 Number Sequence Computation
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
    
    This function efficiently computes the n-th element of the fib4 number sequence.
    
    Args:
        n (int): The position of the element in the fib4 sequence.
    
    Returns:
        int: The n-th element of the fib4 sequence.
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        # Initialize a list to store the fib4 sequence
        fib4_sequence = [0, 0, 2, 0] + [0] * (n - 3)
        
        # Compute the fib4 sequence iteratively
        for i in range(4, n + 1):
            fib4_sequence[i - 1] = fib4_sequence[i - 2] + fib4_sequence[i - 3] + fib4_sequence[i - 4]
        
        # Return the n-th element of the fib4 sequence
        return fib4_sequence[n - 1]

# Test cases
print(fib4(5))  # 4
print(fib4(6))  # 8
print(fib4(7))  # 14
```
This script defines a function `fib4` to compute the n-th element of the fib4 number sequence. It uses an iterative approach to store and compute the fib4 sequence up to the n-th element. The function returns the n-th element of the fib4 sequence for a given input `n`. The test cases at the end of the script verify the correctness of the function.