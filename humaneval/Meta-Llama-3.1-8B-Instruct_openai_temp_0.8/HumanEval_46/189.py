```python
def fib4(n: int) -> int:
    """
    The Fib4 number sequence is a sequence similar to the Fibbonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    Args:
        n (int): The index of the Fib4 number to compute.
    
    Returns:
        int: The n-th element of the Fib4 number sequence.
    """
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    
    # Initialize a list to store the computed values
    fib4_values = [0, 0, 2, 0]
    
    # Compute the values iteratively
    for i in range(4, n + 1):
        # Calculate the next value in the sequence
        next_value = fib4_values[i - 1] + fib4_values[i - 2] + fib4_values[i - 3] + fib4_values[i - 4]
        # Append the next value to the list
        fib4_values.append(next_value)
    
    # Return the n-th element of the sequence
    return fib4_values[n]
```

Alternatively, you can use a more efficient approach by using a matrix exponentiation to compute the n-th Fibonacci number in O(log n) time complexity:

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

def fib4(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0

    fib_matrix = [[1, 1], [1, 0]]
    identity_matrix = [[1, 0], [0, 1]]

    fib_matrix = matrix_power(fib_matrix, n - 2)
    result_matrix = multiply_matrices(fib_matrix, [[1, 1], [1, 0]])
    result = result_matrix[0][0] * 2 + result_matrix[1][0]

    return result
```

This approach has a much better performance than the naive iterative approach for large values of n.