

def fib4(n: int):
    """The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """
    # We can use dynamic programming to solve this problem, so we don't need recursion.
    # The idea is to use a 4x4 matrix to store the values of fib4(i), i <= n, and update it in each iteration.
    # Then we will return the value of fib4(n) by looking at the upper-left corner of the matrix.

    # Initialize the matrix with zeros
    matrix = [[0] * 4 for _ in range(4)]

    # Loop through the values of fib4(i) and store them in the matrix
    for i in range(4):
        matrix[i][i] = i
        for j in range(i + 1, 4):
            matrix[i][j] = matrix[i][j - 1] + matrix[i - 1][j] + matrix[i - 2][j - 1] + matrix[i - 3][j - 2]

    return matrix[0][3] + matrix[1][3] + matrix[2][3] + matrix[3][2]
