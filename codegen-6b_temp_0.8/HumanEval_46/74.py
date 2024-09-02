

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
    fib4_mtx = [[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1],[0,0,0,0,0],[0,0,0,0,0]]
    if n<5:
        return fib4_mtx[n]
    else:
        for i in range(5,n+1):
            fib4_mtx[i][0] = fib4_mtx[i-1][1] + fib4_mtx[i-2][1] + fib4_mtx[i-3][1] + fib4_mtx[i-4][1]
            fib4_mtx[i][1] = fib4_mtx[i-1][2] + fib4_mtx[i-2][0] + fib4_mtx[i-3][0] + fib4_mtx[i-4][0]
            fib4_mtx[i][2] = fib4_mtx[i-1][3] + fib4_mtx[i-2][1] + fib4_mtx[i-3][2] + fib4_mtx[i-4][1]
            fib4_mtx[i][3] = fib4_mtx[i-1][4] + fib4_mtx[i-2][2] + fib4_mtx[i-3][3] + fib4_mtx[i-4][2]
            fib4_mtx[i][4] = fib4_mtx[i-1][3] + fib4_mtx[i-2][3] + fib4_mtx[i-3][4] + fib4_mtx[i-4][3]

    return fib4_mtx[n]
