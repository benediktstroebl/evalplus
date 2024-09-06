

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
    # throw an error if n is less than 0
    if n < 0:
        raise ValueError
    # declare the first four Fib4 values
    fib4_values = [0, 0, 2, 0]
    # keep track of the last four Fib4 values
    # at each iteration, we'll add the next value of the sequence
    prev_value = 0
    for i in range(4, n+1):
        # this is the next value of the sequence
        curr_value = fib4_values[i-1] + fib4_values[i-2] + fib4_values[i-3] + fib4_values[i-4]
        fib4_values.append(curr_value)
        # store the previous value of the sequence
        prev_value = curr_value
    return fib4_values[n]

