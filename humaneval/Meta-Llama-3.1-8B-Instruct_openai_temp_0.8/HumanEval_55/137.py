```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number to return.

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
        return fib(n-1) + fib(n-2)


# Test the function
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

However, this recursive solution is not efficient for large inputs due to repeated calculations. A more efficient solution can be achieved using dynamic programming, where we store the Fibonacci numbers as we calculate them and reuse them as needed:

```python
def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number to return.

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

    fib_numbers = [0, 1]
    for i in range(2, n+1):
        fib_numbers.append(fib_numbers[i-1] + fib_numbers[i-2])

    return fib_numbers[n]


# Test the function
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

Alternatively, you can use matrix exponentiation to calculate the n-th Fibonacci number in O(log n) time complexity:

```python
def multiply_matrices(a, b):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += a[i][k] * b[k][j]
    return result


def power(matrix, n):
    if n == 1:
        return matrix
    if n % 2 == 0:
        half_pow = power(matrix, n // 2)
        return multiply_matrices(half_pow, half_pow)
    else:
        half_pow = power(matrix, n // 2)
        return multiply_matrices(multiply_matrices(half_pow, half_pow), matrix)


def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number to return.

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
    result_matrix = power(fib_matrix, n - 1)
    return result_matrix[0][0]


# Test the function
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This solution uses matrix exponentiation to calculate the n-th Fibonacci number in O(log n) time complexity, making it more efficient for large inputs.