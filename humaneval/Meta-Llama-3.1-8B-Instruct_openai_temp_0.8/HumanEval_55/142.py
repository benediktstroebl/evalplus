```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number to return.

    Returns:
    int: The n-th Fibonacci number.

    Examples:
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

# Test the function
print(fib(10))  # 55
print(fib(1))   # 1
print(fib(8))   # 21
```

This script defines a recursive function `fib(n)` to calculate the n-th Fibonacci number. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two. The function uses a loop to efficiently calculate the nth Fibonacci number, rather than using recursion which would be inefficient for large values of n due to repeated calculations.

However, the above script is not the most efficient solution if you want to calculate large Fibonacci numbers. A more efficient solution would use matrix exponentiation or the fast doubling method.

Here's the improved function for large n:
```python
def multiply_matrices(a, b):
    """Multiply two 2x2 matrices a and b."""
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += a[i][k] * b[k][j]
    return result


def matrix_power(matrix, n):
    """Calculate the nth power of the 2x2 matrix."""
    if n <= 1:
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
    n (int): The position of the Fibonacci number to return.

    Returns:
    int: The n-th Fibonacci number.

    Examples:
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 1

    # Base matrix
    base_matrix = [[1, 1], [1, 0]]

    # Matrix power
    result_matrix = matrix_power(base_matrix, n - 1)

    # Return the result
    return result_matrix[0][0]

# Test the function
print(fib(10))  # 55
print(fib(1))   # 1
print(fib(8))   # 21
```
This improved function uses matrix exponentiation to efficiently calculate the nth Fibonacci number. It has a time complexity of O(log n) making it much faster than the previous function for large values of n.