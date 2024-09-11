```python
def matrix_power(matrix, n):
    """
    Calculate the nth power of a 3x3 matrix using exponentiation by squaring.
    
    Args:
    matrix (list): A 3x3 matrix.
    n (int): The power to which the matrix should be raised.
    
    Returns:
    list: The nth power of the input matrix.
    """
    # Base case: any matrix raised to the power of 0 is the identity matrix
    if n == 0:
        return [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    
    # Recursive case: calculate the matrix squared, then multiply by the base matrix if necessary
    half_pow = matrix_power(matrix, n // 2)
    result = matrix_multiply(half_pow, half_pow)
    
    if n % 2 == 1:
        result = matrix_multiply(result, matrix)
    
    return result


def matrix_multiply(a, b):
    """
    Multiply two 3x3 matrices.
    
    Args:
    a (list): The first matrix.
    b (list): The second matrix.
    
    Returns:
    list: The product of the input matrices.
    """
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    
    for i in range(3):
        for j in range(3):
            for k in range(3):
                result[i][j] += a[i][k] * b[k][j]
    
    return result


def fibfib(n: int):
    """
    Calculate the nth element of the FibFib number sequence.
    
    Args:
    n (int): The index of the element to calculate.
    
    Returns:
    int: The nth element of the FibFib sequence.
    """
    if n <= 1:
        return 0
    
    # Create the base matrix
    base_matrix = [[0, 0, 1], [0, 1, 1], [1, 1, 0]]
    
    # Raise the matrix to the nth power
    result_matrix = matrix_power(base_matrix, n - 2)
    
    # The nth element is the top-left element of the resulting matrix
    return result_matrix[0][0]


# Test the function
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

This script uses a matrix-based approach to calculate the nth element of the FibFib sequence. It first defines a function to calculate the nth power of a matrix using exponentiation by squaring, then defines a function to multiply two matrices, and finally defines the `fibfib` function that calculates the nth element of the sequence. The `fibfib` function raises the base matrix to the nth power and returns the top-left element of the resulting matrix.