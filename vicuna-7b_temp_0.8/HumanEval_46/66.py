

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
    n_1, n_2, n_3, n_4 = [0] * 4
    n_5, n_6, n_7, n_8 = [0] * 4

    # initialize the fibonacci sequence
    for i in range(8):
        if i < 4:
            n_i = 0
        else:
            n_i = 1
            n_i_plus_1 = 1
            n_i_plus_2 = 1
            n_i_plus_3 = 2
            n_i_plus_4 = 1
            n_i_plus_5 = 1
            n_i_plus_6 = 0
            n_i_plus_7 = 1
            n_i_plus_8 = 1
        n_i_plus_1_plus_2 = n_i_plus_1 + n_i_plus_2
        n_i_plus_1_plus_3 = n_i_plus_1 + n_i_plus_3
        n_i_plus_1_plus_4 = n_i_plus_1 + n_i_plus_4
        n_i_plus_1_plus_5 = n_i_plus_1 + n_i_plus_5
        n_i_plus_1_plus_6 = n_i_plus_1 + n_i_plus_6
        n_i_plus_1_plus_7 = n_i_plus_1 + n_i_plus_7
        n_i_plus_1_plus_8 = n_i_plus_1 + n_i_plus_8
        n_i_plus_2_plus_3 = n_i_plus_2 + n_i_plus_3
        n_i_plus_2_plus_4 = n_i_plus_2 + n_i_plus_4
        n_i_plus_2_plus_5 = n_i_plus_2 + n_i_plus_5
        n_i_plus_2_plus_6 = n_i_plus_2 + n_i_plus_6
        n
