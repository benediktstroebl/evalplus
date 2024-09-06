

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
    if n < 0:
        raise ValueError
    fib4_list = []
    fib4_list.append(0)
    fib4_list.append(0)
    fib4_list.append(2)
    fib4_list.append(0)
    if n > 3:
        for _ in range(n-3):
            fib4_list.append(fib4_list[-1] + fib4_list[-2] + fib4_list[-3] + fib4_list[-4])
    return fib4_list[n]
