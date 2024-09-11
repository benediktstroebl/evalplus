```python
def fibfabonacci_matrix_multiply(matrix, n):
    """Multiply two 2x2 matrices and return the result."""
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += matrix[i][k] * n[k][j]
    return result

def matrix_power(matrix, n):
    """Compute the nth power of a 2x2 matrix using matrix exponentiation."""
    if n == 1:
        return matrix
    if n % 2 == 0:
        half_pow = matrix_power(matrix, n // 2)
        return fibfabonacci_matrix_multiply(half_pow, half_pow)
    else:
        half_pow = matrix_power(matrix, n // 2)
        return fibfabonacci_matrix_multiply(fibfabonacci_matrix_multiply(half_pow, half_pow), matrix)

def fibfabonacci(n):
    """Compute the nth element of the fibfabonacci sequence using matrix exponentiation."""
    if n <= 1:
        return 0
    fib_matrix = [[1, 1], [1, 0]]
    result_matrix = matrix_power(fib_matrix, n - 1)
    return result_matrix[0][0]

# Test the function
for i in range(1, 9):
    print(f"fibfabonacci({i}) = {fibfabonacci(i)}")
```

This script defines the `fibfabonacci` function using matrix exponentiation, which is an efficient method for computing the nth element of the fibfabonacci sequence. The `matrix_power` function computes the nth power of a 2x2 matrix, and the `fibfabonacci_matrix_multiply` function multiplies two 2x2 matrices. The script also includes a test loop that prints the first 8 elements of the fibfabonacci sequence.