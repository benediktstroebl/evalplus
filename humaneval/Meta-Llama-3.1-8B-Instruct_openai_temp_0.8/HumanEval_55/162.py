```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
        n (int): The index of the Fibonacci number to return.

    Returns:
        int: The n-th Fibonacci number.

    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


# Example usage:
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

However, this approach has exponential time complexity due to the repeated calculations involved in the recursive calls. For larger values of `n`, this will be very inefficient.

Here's an iterative approach that uses a loop and has linear time complexity:

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
        n (int): The index of the Fibonacci number to return.

    Returns:
        int: The n-th Fibonacci number.

    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 1:
        return n

    fib_prev = 0
    fib_curr = 1

    for _ in range(2, n + 1):
        fib_next = fib_prev + fib_curr
        fib_prev = fib_curr
        fib_curr = fib_next

    return fib_curr


# Example usage:
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

Additionally, for large values of `n`, you may want to use the matrix exponentiation method, which has a logarithmic time complexity. Here's an example of how to implement it:

```python
def multiply_matrices(a, b):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += a[i][k] * b[k][j]
    return result


def matrix_power(matrix, n):
    if n == 1:
        return matrix
    if n % 2 == 0:
        half_pow = matrix_power(matrix, n // 2)
        return multiply_matrices(half_pow, half_pow)
    else:
        half_pow = matrix_power(matrix, n // 2)
        return multiply_matrices(multiply_matrices(half_pow, half_pow), matrix)


def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
        n (int): The index of the Fibonacci number to return.

    Returns:
        int: The n-th Fibonacci number.

    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 1:
        return n

    fib_matrix = [[1, 1], [1, 0]]
    result_matrix = matrix_power(fib_matrix, n - 1)
    return result_matrix[0][0]


# Example usage:
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This implementation uses