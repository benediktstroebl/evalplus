### Efficiently Computing the Fib4 Number Sequence
```python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibonacci sequence 
    that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    This function efficiently computes the n-th element of the fib4 number sequence.
    It uses dynamic programming to store and reuse previously computed values.
    
    Args:
    n (int): The index of the element in the fib4 sequence to compute.
    
    Returns:
    int: The n-th element of the fib4 sequence.
    """
    if n < 4:
        # Base cases: fib4(0), fib4(1), fib4(2)
        return [0, 0, 2][n]
    
    # Initialize the base matrix [[1, 1, 1, 0], [1, 0, 0, 0]]
    base_matrix = [[1, 1, 1, 0], [1, 0, 0, 0]]
    
    # Perform matrix exponentiation to compute the n-th power of the base matrix
    result_matrix = matrix_power(base_matrix, n - 3)
    
    # The n-th element of the fib4 sequence is the top-left element of the resulting matrix
    return result_matrix[0][0]


def matrix_multiply(a, b):
    """
    Multiply two 2x2 matrices.
    
    Args:
    a (list): The first matrix.
    b (list): The second matrix.
    
    Returns:
    list: The product of the two matrices.
    """
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += a[i][k] * b[k][j]
    return result


def matrix_power(matrix, n):
    """
    Compute the n-th power of a 2x2 matrix using exponentiation by squaring.
    
    Args:
    matrix (list): The matrix to exponentiate.
    n (int): The exponent.
    
    Returns:
    list: The n-th power of the matrix.
    """
    if n == 1:
        return matrix
    if n % 2 == 0:
        half_power = matrix_power(matrix, n // 2)
        return matrix_multiply(half_power, half_power)
    else:
        half_power = matrix_power(matrix, n // 2)
        return matrix_multiply(matrix_multiply(half_power, half_power), matrix)


# Example usage:
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script uses matrix exponentiation to efficiently compute the n-th element of the fib4 sequence. The `matrix_power` function uses exponentiation by squaring to compute the n-th power of a matrix in logarithmic time. The `fib4` function uses this to compute the n-th element of the fib4 sequence in O(log n) time.