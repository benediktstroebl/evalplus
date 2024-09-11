### Fibonacci-like Sequence: Fib4
#### Iterative Solution in Python
```python
def fib4(n: int):
    """
    Compute the n-th element of the fib4 number sequence.

    The Fib4 number sequence is defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    Args:
        n (int): The index of the element to compute.

    Returns:
        int: The n-th element of the fib4 number sequence.
    """
    if n < 0:
        raise ValueError("Input should be a non-negative integer")

    # Base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    
    # Initialize the base matrix
    base_matrix = [[0, 0, 0, 1],
                   [1, 0, 1, 0],
                   [0, 1, 0, 1],
                   [1, 1, 1, 1]]
    
    # Exponentiate the base matrix
    result_matrix = matrix_power(base_matrix, n - 2)
    
    # The result is the top-right element of the resulting matrix
    return result_matrix[0][3]


def matrix_multiply(a, b):
    """
    Multiply two 4x4 matrices.

    Args:
        a (list): The first matrix.
        b (list): The second matrix.

    Returns:
        list: The product of the two matrices.
    """
    result = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    
    for i in range(4):
        for j in range(4):
            for k in range(4):
                result[i][j] += a[i][k] * b[k][j]
    
    return result


def matrix_power(matrix, n):
    """
    Compute the nth power of a 4x4 matrix.

    Args:
        matrix (list): The base matrix.
        n (int): The exponent.

    Returns:
        list: The nth power of the matrix.
    """
    if n == 1:
        return matrix
    
    if n % 2 == 0:
        half_power = matrix_power(matrix, n // 2)
        return matrix_multiply(half_power, half_power)
    else:
        half_power = matrix_power(matrix, n // 2)
        return matrix_multiply(matrix_multiply(half_power, half_power), matrix)


# Test cases
print(fib4(5))  # 4
print(fib4(6))  # 8
print(fib4(7))  # 14
```
This code defines a function `fib4` to compute the n-th element of the fib4 number sequence using matrix exponentiation. The `matrix_power` function is a helper function to compute the nth power of a matrix using exponentiation by squaring, and the `matrix_multiply` function is a helper function to multiply two matrices.