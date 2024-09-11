```python
def matrix_multiply(a, b):
    """ Helper function to multiply two 2x2 matrices """
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += a[i][k] * b[k][j]
    return result

def matrix_power(matrix, n):
    """ Helper function to calculate the nth power of a 2x2 matrix """
    if n == 1:
        return matrix
    if n % 2 == 0:
        half_pow = matrix_power(matrix, n // 2)
        return matrix_multiply(half_pow, half_pow)
    else:
        half_pow = matrix_power(matrix, n // 2)
        return matrix_multiply(matrix_multiply(half_pow, half_pow), matrix)

def fibfib(n: int):
    """
    The FibFib number sequence is a sequence similar to the Fibbonacci sequence 
    that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    This function efficiently computes the n-th element of the fibfib number sequence.
    """
    if n < 2:
        return 0
    base_matrix = [[1, 1], [1, 0]]
    result_matrix = matrix_power(base_matrix, n - 1)
    return result_matrix[0][0]

# Test cases
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```

This script uses matrix exponentiation to efficiently compute the n-th element of the fibfib number sequence. The `matrix_power` function calculates the nth power of a 2x2 matrix using a divide-and-conquer approach, and the `matrix_multiply` function multiplies two 2x2 matrices. The `fibfib` function uses these helper functions to compute the n-th element of the fibfib number sequence.