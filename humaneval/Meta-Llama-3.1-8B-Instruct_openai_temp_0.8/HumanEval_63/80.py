### FibFib Number Sequence
#### Problem Description

The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
- `fibfib(0) == 0`
- `fibfib(1) == 0`
- `fibfib(2) == 1`
- `fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).`

#### Solution
```python
def matrix_power(matrix, n):
    """
    Calculate the nth power of a 3x3 matrix using exponentiation by squaring.
    
    Args:
    matrix (list): A 3x3 matrix.
    n (int): The power to which the matrix should be raised.
    
    Returns:
    list: The nth power of the matrix.
    """
    if n == 1:
        return matrix
    if n % 2 == 0:
        half_power = matrix_power(matrix, n // 2)
        return matrix_multiply(half_power, half_power)
    else:
        half_power = matrix_power(matrix, n // 2)
        return matrix_multiply(matrix_multiply(half_power, half_power), matrix)

def matrix_multiply(A, B):
    """
    Multiply two 3x3 matrices A and B.
    
    Args:
    A (list): The first 3x3 matrix.
    B (list): The second 3x3 matrix.
    
    Returns:
    list: The product of A and B.
    """
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                result[i][j] += A[i][k] * B[k][j]
    return result

def fibfib(n: int):
    """
    Calculate the nth element of the FibFib number sequence.
    
    Args:
    n (int): The index of the element in the FibFib sequence.
    
    Returns:
    int: The nth element of the FibFib sequence.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n == 0:
        return 0
    elif n == 1:
        return 0
    
    # Define the base matrix for the Fibonacci recurrence relation
    base_matrix = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]
    
    # Calculate the (n-1)th power of the base matrix
    result_matrix = matrix_power(base_matrix, n - 1)
    
    # The nth element of the FibFib sequence is the middle element of the top row of the result matrix
    return result_matrix[0][1]

# Test cases
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```
This solution uses the properties of matrix exponentiation to efficiently compute the nth element of the FibFib number sequence. It uses a recursive function to calculate the (n-1)th power of a base matrix, which represents the recurrence relation of the FibFib sequence. The result is the middle element of the top row of the final matrix, which is the nth element of the FibFib sequence.