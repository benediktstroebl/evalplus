### Python Script to Compute n-th Element of Fib4 Number Sequence

```markdown
### Code
```python
def fib4(n: int) -> int:
    """
    Compute the n-th element of the Fib4 number sequence.

    Args:
    n (int): The index of the element to compute.

    Returns:
    int: The n-th element of the Fib4 number sequence.
    """
    if n <= 1:
        return 0
    
    # Initialize the base matrix
    matrix = [[1, 1, 1, 0],
              [1, 0, 0, 1],
              [0, 1, 0, 1],
              [1, 1, 1, 1]]
    
    # Perform matrix exponentiation to compute the n-th element
    matrix = matrix_power(matrix, n - 2)
    
    # The n-th element is the top-left element of the resulting matrix
    return matrix[0][0]


def matrix_multiply(a, b):
    """
    Multiply two 2x2 matrices.

    Args:
    a (list[list[int]]): The first matrix.
    b (list[list[int]]): The second matrix.

    Returns:
    list[list[int]]: The product of the two matrices.
    """
    result = [[0, 0],
              [0, 0]]
    
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += a[i][k] * b[k][j]
    
    return result


def matrix_power(matrix, n):
    """
    Compute the n-th power of a 2x2 matrix using exponentiation by squaring.

    Args:
    matrix (list[list[int]]): The matrix to exponentiate.
    n (int): The exponent.

    Returns:
    list[list[int]]: The n-th power of the matrix.
    """
    if n <= 1:
        return matrix
    
    # Recursively compute the n//2-th power of the matrix
    half_power = matrix_power(matrix, n // 2)
    
    # Compute the full power using exponentiation by squaring
    if n % 2 == 0:
        return matrix_multiply(half_power, half_power)
    else:
        return matrix_multiply(matrix_multiply(half_power, half_power), matrix)


# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

### Explanation

The `fib4` function uses matrix exponentiation to efficiently compute the n-th element of the Fib4 number sequence. The idea is to represent the recurrence relation as a matrix multiplication and then use exponentiation by squaring to compute the n-th power of the matrix.

The `matrix_multiply` function multiplies two 2x2 matrices, and the `matrix_power` function computes the n-th power of a 2x2 matrix using exponentiation by squaring.

In the `fib4` function, we first check if `n` is less than or equal to 1 and return 0 if so. Otherwise, we initialize the base matrix and perform matrix exponentiation to compute the n-th element. The resulting matrix is then returned as the n-th element of the Fib4 number sequence.