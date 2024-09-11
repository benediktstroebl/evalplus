```python
def fibfib(n: int):
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence 
    that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

    Args:
    n (int): The position of the element in the sequence.

    Returns:
    int: The nth element of the fibfib number sequence.

    Raises:
    ValueError: If n is a negative integer.

    Example:
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
    if n < 0:
        raise ValueError("Input should be a non-negative integer.")
    elif n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        matrix = [[1, 1, 1],
                  [1, 0, 0],
                  [0, 1, 0]]
        result = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]

        for _ in range(n - 2):
            for i in range(3):
                for j in range(3):
                    result[i][j] = matrix[i][0] * matrix[0][j] + \
                                   matrix[i][1] * matrix[1][j] + \
                                   matrix[i][2] * matrix[2][j]
            matrix = result.copy()

        return matrix[0][0]


# Test the function
print(fibfib(1))  # Expected output: 0
print(fibfib(5))  # Expected output: 4
print(fibfib(8))  # Expected output: 24
```
This Python script defines a function `fibfib(n)` that computes the nth element of the fibfib number sequence using matrix exponentiation. The time complexity of this function is O(n), which is more efficient than the naive recursive approach with a time complexity of O(3^n).