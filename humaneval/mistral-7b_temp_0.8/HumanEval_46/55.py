

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
    # Initialize the array
    arr = [0, 0, 2, 0]

    # Check if n is greater than 4
    if n > 4:
        # Iterate from 5 to n
        for i in range(5, n+1):
            # Calculate the value of the n-th element
            arr.append(arr[i-1] + arr[i-2] + arr[i-3] + arr[i-4])

    # Return the n-th element of the fib4 number sequence
    return arr[n]

