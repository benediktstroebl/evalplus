

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

    last_seq = 0
    last_seq_1 = 2
    last_seq_2 = 0
    last_seq_3 = 0
    last_seq_4 = 0
    seq = 0
    if n == 0:
        return seq
    elif n == 1:
        seq = last_seq
        return seq
    elif n == 2:
        seq = last_seq_1
        return seq
    elif n == 3:
        seq = last_seq_2
        return seq
    elif n == 4:
        seq = last_seq_3
        return seq
    elif n == 5:
        seq = last_seq_1 + last_seq_2 + last_seq_3 + last_seq_4
        return seq
    else:
        seq = last_seq_1 + last_seq_2 + last_seq_3 + last_seq_4
        for i in range(n):
            last_seq_1 = last_seq_2
            last_seq_2 = last_seq_3
            last_seq_3 = last_seq
