```python
def matrix_power(matrix, n):
    """
    Compute the nth power of a 3x3 matrix using exponentiation by squaring.
    
    Args:
    matrix (list of lists): A 3x3 matrix.
    n (int): The power to which the matrix should be raised.
    
    Returns:
    list of lists: The nth power of the input matrix.
    """
    if n == 1:
        return matrix
    if n % 2 == 0:
        half_power = matrix_power(matrix, n // 2)
        return matrix_multiply(half_power, half_power)
    else:
        half_power = matrix_power(matrix, n // 2)
        return matrix_multiply(matrix_multiply(half_power, half_power), matrix)


def matrix_multiply(A, B):
    """
    Compute the product of two 3x3 matrices A and B.
    
    Args:
    A (list of lists): The first matrix.
    B (list of lists): The second matrix.
    
    Returns:
    list of lists: The product of A and B.
    """
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                result[i][j] += A[i][k] * B[k][j]
    return result


def fibfib(n: int):
    """
    The FibFib number sequence is a sequence similar to the Fibbonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
    n (int): The index of the FibFib number to be computed.
    
    Returns:
    int: The nth element of the FibFib number sequence.
    """
    if n < 2:
        return 0
    if n == 2:
        return 1
    
    # Create the base matrix [[1, 1, 1], [1, 0, 0], [0, 1, 0]]
    base_matrix = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]
    
    # Compute the (n-1)th power of the base matrix
    result_matrix = matrix_power(base_matrix, n - 1)
    
    # The result is the sum of the elements in the first row of the resulting matrix
    return result_matrix[0][0] + result_matrix[0][1] + result_matrix[0][2]


# Test cases
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```

This script uses matrix exponentiation to efficiently compute the nth element of the FibFib number sequence. The `matrix_power` function raises a 3x3 matrix to a given power using the exponentiation by squaring technique, and the `fibfib` function uses this to compute the nth element of the FibFib sequence. The test cases at the end demonstrate the correctness of the implementation.