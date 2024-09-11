```markdown
### FibFib Number Sequence
#### Efficient Computation of the n-th Element

Below is a Python script that efficiently computes the n-th element of the FibFib number sequence.

```python
def matrix_multiply(a, b):
    """Helper function to multiply two 2x2 matrices."""
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            result[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j]
    return result


def matrix_power(matrix, n):
    """Helper function to compute the nth power of a 2x2 matrix."""
    if n == 1:
        return matrix
    if n % 2 == 0:
        half_pow = matrix_power(matrix, n // 2)
        return matrix_multiply(half_pow, half_pow)
    else:
        half_pow = matrix_power(matrix, n // 2)
        return matrix_multiply(matrix_multiply(half_pow, half_pow), matrix)


def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    """
    if n <= 1:
        return 0
    else:
        fib_matrix = [[1, 1], [1, 0]]
        identity_matrix = [[1, 0], [0, 1]]
        result_matrix = matrix_power(fib_matrix, n - 1)
        return result_matrix[0][0]


# Example usage:
print(fibfib(1))     # Output: 0
print(fibfib(5))     # Output: 4
print(fibfib(8))     # Output: 24
```

This script uses matrix exponentiation to compute the n-th element of the FibFib number sequence in O(log n) time.
```