

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
    # Create an empty list to store the sequence
    fib4_sequence = []
    
    # Loop through the sequence and add the current element to the list
    for i in range(n):
        fib4_sequence.append(fib4_sequence[-1])
    
    # Remove the first element from the list
    fib4_sequence.pop(0)
    
    return fib4_sequence[-1]