

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

    if n <= 1:
        return n
    #return the first 4 elements
    if n == 2:
        return 2
    if n == 3:
        return 0
    if n == 4:
        return 4

    #append next element to the sequence
    #i dont think this is right, it is not returning the right sequence
    seq = [2,0,4]
    n -= 3
    while n > 0:
        seq.append(seq[n-1] + seq[n-2] + seq[n-3] + seq[n-4])
        n -= 1
    return seq[-1]
