

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
    # fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)
    # fib4(n) = 2fib4(n-2) + 3fib4(n-4)
    # fib4(n) = P(n)fib4(0) + Q(n)fib4(1)
    # 2Q(n) + Q(n-1) = Q(n) + 2P(n)
    # Q(n) = P(n-1) - Q(n-1)
    # Q(0) = 0, Q(1) = 1

    Q = [0, 1]
    P = [2, 3]

    for i in range(2, n+1):
        new_Q = Q[i-1] - Q[i-2]
        Q.append(new_Q)
        new_P = Q[i] + 2*P[i-1]
        P.append(new_P)
    return P[n]
