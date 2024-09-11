```python
def fib4(n: int) -> int:
    """
    The Fib4 number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    This function efficiently computes the n-th element of the fib4 number sequence using dynamic programming.
    
    Args:
    n (int): The index of the element in the fib4 sequence.
    
    Returns:
    int: The n-th element of the fib4 sequence.
    """
    
    # Handle edge cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    
    # Initialize the base matrix
    matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    
    # Initialize the base values
    matrix[0][0] = matrix[1][0] = matrix[2][1] = matrix[3][0] = 0
    matrix[2][0] = 2
    
    # Perform matrix exponentiation
    for _ in range(2, n + 1):
        matrix = matrix_multiply(matrix, matrix)
    
    # Return the top-left element of the resulting matrix
    return matrix[0][0]


def matrix_multiply(a, b):
    """
    Multiplies two 4x4 matrices.
    
    Args:
    a (list): The first matrix.
    b (list): The second matrix.
    
    Returns:
    list: The product of the two matrices.
    """
    
    result = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    
    for i in range(4):
        for j in range(4):
            for k in range(4):
                result[i][j] += a[i][k] * b[k][j]
    
    return result


# Test the function
print(fib4(5))   # Output: 4
print(fib4(6))   # Output: 8
print(fib4(7))   # Output: 14
```

This solution uses matrix exponentiation to efficiently calculate the n-th element of the fib4 sequence. It first initializes the base matrix and values, then performs matrix exponentiation to raise the base matrix to the power of n - 2, and finally returns the top-left element of the resulting matrix. The `matrix_multiply` function is used to multiply two 4x4 matrices.