### Fibonacci Number Calculator
#### Using Memoization for Efficient Computation

```python
def fib(n: int) -> int:
    """Return n-th Fibonacci number.
    
    Args:
        n (int): Position of the Fibonacci number to be calculated.
    
    Returns:
        int: n-th Fibonacci number.
    
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    memo = {0: 0, 1: 1}
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]

# Example usage:
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This script uses a technique called memoization to store and reuse previously computed Fibonacci numbers. This approach significantly reduces the computational time and memory usage compared to a naive recursive implementation, especially for large inputs.

However, for very large inputs, an even more efficient approach would be to use the matrix exponentiation method, which has a time complexity of O(log n). Here's an example implementation:

```python
def multiply_matrices(a, b):
    """Multiply two 2x2 matrices."""
    result = [[0, 0], [0, 0]]
    result[0][0] = a[0][0] * b[0][0] + a[0][1] * b[1][0]
    result[0][1] = a[0][0] * b[0][1] + a[0][1] * b[1][1]
    result[1][0] = a[1][0] * b[0][0] + a[1][1] * b[1][0]
    result[1][1] = a[1][0] * b[0][1] + a[1][1] * b[1][1]
    return result

def matrix_power(matrix, n):
    """Compute the nth power of a 2x2 matrix."""
    if n == 1:
        return matrix
    if n % 2 == 0:
        half_pow = matrix_power(matrix, n // 2)
        return multiply_matrices(half_pow, half_pow)
    else:
        half_pow = matrix_power(matrix, n // 2)
        return multiply_matrices(multiply_matrices(half_pow, half_pow), matrix)

def fib(n: int) -> int:
    """Return n-th Fibonacci number using matrix exponentiation."""
    if n < 2:
        return n
    matrix = [[1, 1], [1, 0]]
    result_matrix = matrix_power(matrix, n - 1)
    return result_matrix[0][0]

# Example usage:
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
```

This implementation has a time complexity of O(log n) and is more efficient than the memoized approach for large inputs.