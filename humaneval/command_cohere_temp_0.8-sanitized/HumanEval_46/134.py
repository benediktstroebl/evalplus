def fib4(n: int) -> int:
    """
    The Fib4 number sequence is a sequence similar to the Fibbonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Returns the n-th element of the Fib4 sequence. 
    """
    # Initializing res to the first 4 values of the sequence
    res = [0, 0, 2, 0]

    # Building the sequence up to nth index using a loop
    for i in range(4, n+1):
        res.append(res[i-1] + res[i-2] + res[i-3] + res[i-4])

    return res[n]