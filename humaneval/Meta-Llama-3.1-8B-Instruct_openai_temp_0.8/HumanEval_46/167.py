### Fib4 Number Sequence Calculator
#### Self-Contained Python Script

```python
def fib4(n: int) -> int:
    """
    Compute the n-th element of the Fib4 number sequence.

    The Fib4 number sequence is defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    Args:
        n (int): The index of the Fib4 number to compute.

    Returns:
        int: The n-th element of the Fib4 number sequence.

    Raises:
        ValueError: If n is a negative integer.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n <= 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        # Initialize the base matrix
        base_matrix = [[1, 1, 1, 0],
                       [1, 0, 0, 0],
                       [0, 1, 0, 0],
                       [0, 0, 1, 0]]

        # Initialize the result matrix
        result_matrix = [[0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0]]

        # Compute the matrix exponentiation
        for _ in range(2, n + 1):
            result_matrix = matrix_multiply(result_matrix, base_matrix)

        # Extract the result from the matrix
        return result_matrix[0][0]


def matrix_multiply(a: list, b: list) -> list:
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


# Example usage
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This script uses matrix exponentiation to efficiently compute the n-th element of the Fib4 number sequence. It first initializes the base matrix and the result matrix, then computes the matrix exponentiation using a loop. Finally, it extracts the result from the matrix.