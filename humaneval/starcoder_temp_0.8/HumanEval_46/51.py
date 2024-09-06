

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
    # Base case:
    if n < 0:
        return None

    # We'll represent the sequence with an array and use zero-based indexing:
    sequence = [0, 0, 2, 0]
    i = 3
    while i <= n:
        # Define the new sequence
        new_sequence = [0] * (i+1)
        new_sequence[0] = 0
        new_sequence[1] = 0
        new_sequence[2] = 2
        j = 3
        while j < i:
            new_sequence[j] = sequence[j-1] + sequence[j-2] + sequence[j-3] + sequence[j-4]
            j += 1
        sequence = new_sequence
        i += 1

    # Return the final element of the sequence
    return sequence[-1]

