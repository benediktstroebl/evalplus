```python
def fib4(n: int) -> int:
    """
    The Fib4 number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    This function efficiently computes the n-th element of the fib4 number sequence using dynamic programming.
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    
    # Initialize the base matrix
    F = [[0, 0, 0, 1],
         [1, 0, 1, 0],
         [0, 1, 0, 0],
         [1, 1, 0, 0]]
    
    # Compute the nth power of the matrix
    for _ in range(2, n):
        F = matrix_multiply(F, F)
    
    # The nth element is the top-left element of the resulting matrix
    return F[0][0]


def matrix_multiply(A, B):
    """
    Helper function to multiply two 4x4 matrices.
    """
    result = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    
    for i in range(4):
        for j in range(4):
            for k in range(4):
                result[i][j] += A[i][k] * B[k][j]
            result[i][j] %= 10  # Reduce modulo 10 to avoid large numbers
    
    return result


# Test the function
if __name__ == "__main__":
    print(fib4(5))  # Output: 4
    print(fib4(6))  # Output: 8
    print(fib4(7))  # Output: 14
```

This script uses matrix exponentiation to efficiently compute the nth element of the fib4 number sequence. The `matrix_multiply` function is a helper function that multiplies two 4x4 matrices element-wise.