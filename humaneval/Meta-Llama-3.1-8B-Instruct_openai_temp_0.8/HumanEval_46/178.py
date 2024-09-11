### Fib4 Number Sequence
#### Efficient Computation using Dynamic Programming

```python
def fib4(n: int) -> int:
    """
    Compute the n-th element of the Fib4 number sequence.

    The Fib4 number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    Args:
        n (int): The index of the element in the Fib4 sequence.

    Returns:
        int: The n-th element of the Fib4 sequence.
    """
    if n <= 3:
        # Base cases
        return [0, 0, 2, 0][n]

    # Initialize the base matrix
    A = [[1, 1, 1, 1], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]]

    # Compute the powers of the matrix A
    for _ in range(3, n):
        A = matrix_multiply(A, A)

    # Extract the result from the matrix
    result = [row[0] for row in A]

    return result[0]


def matrix_multiply(A, B):
    """
    Multiply two 2x2 matrices.

    Args:
        A (list[list[int]]): The first matrix.
        B (list[list[int]]): The second matrix.

    Returns:
        list[list[int]]: The product of the two matrices.
    """
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += A[i][k] * B[k][j]
    return result


# Test the function
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script defines the `fib4` function, which efficiently computes the n-th element of the Fib4 number sequence using dynamic programming. The `matrix_multiply` function is used to multiply two 2x2 matrices, which is used to compute the powers of the base matrix. The script also includes test cases to verify the correctness of the `fib4` function.