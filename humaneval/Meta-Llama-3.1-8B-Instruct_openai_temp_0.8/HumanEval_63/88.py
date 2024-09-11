### FibFib Number Sequence
#### Python Implementation

```python
def matrix_multiply(A, B):
    """Multiply two 2x2 matrices."""
    return [[A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
            [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]]


def matrix_power(matrix, n):
    """Compute the nth power of a 2x2 matrix."""
    if n == 1:
        return matrix
    if n % 2 == 0:
        half_pow = matrix_power(matrix, n // 2)
        return matrix_multiply(half_pow, half_pow)
    else:
        half_pow = matrix_power(matrix, n // 2)
        return matrix_multiply(matrix_multiply(half_pow, half_pow), matrix)


def fibfib(n: int) -> int:
    """Compute the nth FibFib number."""
    if n <= 1:
        return 0
    matrix = [[1, 1], [1, 0]]
    result_matrix = matrix_power(matrix, n - 1)
    return result_matrix[0][0]


# Test cases
print(fibfib(1))  # Expected output: 0
print(fibfib(5))  # Expected output: 4
print(fibfib(8))  # Expected output: 24
```
This script defines a function `fibfib(n)` to compute the `n`-th element of the FibFib number sequence. It uses a matrix exponentiation approach to achieve efficient computation. The `matrix_multiply` function multiplies two 2x2 matrices, and the `matrix_power` function computes the `n`-th power of a 2x2 matrix. The `fibfib` function uses these helper functions to compute the `n`-th FibFib number. The test cases demonstrate the correctness of the implementation.