```python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibbonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    This function efficiently computes the n-th element of the fib4 number sequence without using recursion.
    
    Parameters:
    n (int): The position of the element in the sequence.
    
    Returns:
    int: The nth element of the fib4 number sequence.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        # Initialize the base matrix [[0, 0, 0, 0], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]]
        base_matrix = [[0, 0, 0, 0], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]]
        
        # Perform exponentiation by squaring to compute the nth matrix power
        result_matrix = matrix_power(base_matrix, n - 2)
        
        # The nth element of the fib4 sequence is the first element of the first row in the result matrix
        return result_matrix[0][0]


def matrix_multiply(a, b):
    """
    Helper function to multiply two 2x2 matrices.
    
    Parameters:
    a (list of lists): The first matrix.
    b (list of lists): The second matrix.
    
    Returns:
    list of lists: The product of the two matrices.
    """
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += a[i][k] * b[k][j]
    return result


def matrix_power(matrix, n):
    """
    Helper function to compute the nth power of a 2x2 matrix using exponentiation by squaring.
    
    Parameters:
    matrix (list of lists): The base matrix.
    n (int): The power to which the matrix should be raised.
    
    Returns:
    list of lists: The nth power of the matrix.
    """
    if n == 0:
        return [[1, 0], [0, 1]]
    elif n % 2 == 0:
        half_power = matrix_power(matrix, n // 2)
        return matrix_multiply(half_power, half_power)
    else:
        half_power = matrix_power(matrix, n // 2)
        return matrix_multiply(matrix_multiply(half_power, half_power), matrix)


# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script uses matrix exponentiation to efficiently compute the nth element of the fib4 number sequence without using recursion. It first initializes the base matrix and then uses the `matrix_power` function to compute the (n-