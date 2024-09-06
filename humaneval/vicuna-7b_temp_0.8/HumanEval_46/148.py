

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
    # Use dynamic programming to store the sum of fibonacci numbers up to the current index
    # and fib4(0) = 0
    # fib4(1) = 0
    dp = [[0] * (n+1) for _ in range(4)]
    dp[0][0] = 0
    dp[0][1] = 0
    dp[1][0] = 1
    dp[1][1] = 1
    dp[2][0] = 1
    dp[2][1] = 1
    dp[3][0] = 1
    dp[3][1] = 2
    dp[4][0] = 1
    dp[4][1] = 2
    dp[5][0] = 1
    dp[5][1] = 3
    dp[6][0] = 1
    dp[6][1] = 3
    dp[7][0] = 1
    dp[7][1] = 5
    dp[8][0] = 1
    dp[8][1] = 5
    dp[9][0] = 1
    dp[9][1] = 8
    dp[10][0] = 2
    dp[10][1] = 10
    dp[11][0] = 2
    dp[11][1] = 10
    dp[12][0] = 2
    dp[12][1] = 14
    dp[13][0] = 3
    dp[13][1] = 16
    dp[14][0] = 3
    dp[14][1] = 16
    dp[15][0] = 3
    dp[15][1] = 20
    dp[16][0] = 4
    dp[16][1] = 22
    dp[17][0] = 4
    dp[17
