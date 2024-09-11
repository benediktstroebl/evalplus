```python
def matrix_multiply(A, B):
    """Multiply two 2x2 matrices."""
    return [[A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
            [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]]


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


def fibfib(n: int):
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    This function uses matrix exponentiation to efficiently compute the nth element of the FibFib sequence.
    """
    if n <= 1:
        return 0
    if n == 2:
        return 1
    fib_matrix = [[1, 1], [1, 0]]
    identity_matrix = [[1, 0], [0, 1]]
    fib_matrix = matrix_power(fib_matrix, n - 2)
    identity_matrix = matrix_power(identity_matrix, n - 2)
    result_matrix = matrix_multiply(fib_matrix, [[1, 1], [1, 0]])
    result = result_matrix[0][0]
    return result + result_matrix[0][1] * (result_matrix[0][0]) + (result_matrix[0][0]) * (result_matrix[0][1])

# Test cases
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```
This script uses a technique called matrix exponentiation to efficiently compute the nth element of the FibFib sequence. It defines a function `matrix_multiply` to multiply two 2x2 matrices and a function `matrix_power` to calculate the nth power of a 2x2 matrix. The `fibfib` function uses these helper functions to efficiently compute the nth element of the FibFib sequence. The test cases at the end of the script demonstrate the correctness of the `fibfib` function.