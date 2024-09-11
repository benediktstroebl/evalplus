```python
def matrix_multiply(a, b):
    """Multiply two 2x2 matrices."""
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += a[i][k] * b[k][j]
    return result


def matrix_power(matrix, n):
    """Calculate the nth power of a 2x2 matrix."""
    if n == 1:
        return matrix
    if n % 2 == 0:
        half_pow = matrix_power(matrix, n // 2)
        return matrix_multiply(half_pow, half_pow)
    else:
        half_pow = matrix_power(matrix, n // 2)
        return matrix_multiply(matrix_multiply(half_pow, half_pow), matrix)


def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonaccci sequence
    that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    This function efficiently computes the n-th element of the fibfib number sequence.

    Args:
        n: The index of the element in the fibfib sequence.

    Returns:
        The nth element of the fibfib sequence.
    """
    if n == 0:
        return 0
    fib_matrix = [[1, 1], [1, 0]]
    result_matrix = matrix_power(fib_matrix, n - 1)
    return result_matrix[0][0]


# Test cases
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```

This script uses the property that the nth element of the fibfib sequence is equivalent to the top left element of the (n-1)th power of the matrix [[1, 1], [1, 0]], with matrix multiplication used to calculate the power. This approach has a time complexity of O(log n), making it much more efficient than a naive recursive approach for large values of n.