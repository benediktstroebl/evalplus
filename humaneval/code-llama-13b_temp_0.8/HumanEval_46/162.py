

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
    """
    Ideas:
    To solve this problem, I could use a simple brute force method.
    Another approach would be to use a dynamic programming approach.
    The third approach would be to use a matrix approach
    The fourth approach would be to use a matrix approach and then realize that we can use exponentiation of matrices to compute the sequence.
    """
    # create the matrix to hold the fib4 sequence
    matrix = [[0, 0, 2, 0], [0, 0, 0, 2], [2, 0, 0, 0], [0, 2, 0, 0]]

    # get the nth power of the matrix
    result = matrix
    for i in range(n-1):
        result = multiply_matrices(result, matrix)

    # the first row of the nth power matrix will hold the fib4 sequence
    return result[0][0]

