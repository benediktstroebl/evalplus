```python
def fib4(n: int):
    """The Fib4 number sequence is a sequence similar to the Fibbonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.

    :param n: The index of the element to compute in the Fib4 sequence.
    :return: The n-th element of the Fib4 sequence.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    
    # Initialize a list to store the computed elements
    fib4_sequence = [0, 0, 2] + [0]*(n-2)
    
    # Compute the elements of the sequence iteratively
    for i in range(4, n+1):
        fib4_sequence[i-1] = fib4_sequence[i-2] + fib4_sequence[i-3] + fib4_sequence[i-4]
    
    # Return the nth element
    return fib4_sequence[n-1]

# Test cases
print(fib4(5))  # 4
print(fib4(6))  # 8
print(fib4(7))  # 14
```

This script defines a function `fib4(n)` that computes the nth element of the Fib4 number sequence. The function uses an iterative approach to compute the elements of the sequence, rather than recursion. It first checks for the base cases, then initializes a list to store the computed elements. It fills the list with the computed elements using a loop, and finally returns the nth element.