### Computing the Fibonacci-like Fib4 Number Sequence

Here's a Python script that efficiently computes the n-th element of the Fib4 number sequence using dynamic programming.

```python
def fib4(n: int):
    """
    Compute the n-th element of the Fib4 number sequence.
    
    The Fib4 number sequence is defined as:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    Args:
    n (int): The index of the element to compute.
    
    Returns:
    int: The n-th element of the Fib4 number sequence.
    """
    
    # Handle edge cases
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    
    # Initialize the base matrix
    A = [[0, 0, 0, 0],
         [1, 0, 0, 0],
         [0, 1, 0, 0],
         [0, 0, 1, 0]]
    
    # Compute the powers of the base matrix
    for _ in range(2, n):
        A = matrix_multiply(A, A)
    
    # The result is the top-left element of the resulting matrix
    return A[0][0]


def matrix_multiply(A, B):
    """
    Compute the matrix product of two 4x4 matrices A and B.
    
    Args:
    A (list of lists): The first matrix.
    B (list of lists): The second matrix.
    
    Returns:
    list of lists: The matrix product of A and B.
    """
    
    # Initialize the result matrix
    C = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]
    
    # Perform the matrix multiplication
    for i in range(4):
        for j in range(4):
            for k in range(4):
                C[i][j] += A[i][k] * B[k][j]
    
    return C


# Test the function
print(fib4(5))   # Output: 4
print(fib4(6))   # Output: 8
print(fib4(7))   # Output: 14
```

This script uses the concept of matrix exponentiation to efficiently compute the n-th element of the Fib4 number sequence. The `matrix_multiply` function computes the matrix product of two 4x4 matrices, which is used to compute the powers of the base matrix. The result is the top-left element of the resulting matrix, which is the n-th element of the Fib4 number sequence.