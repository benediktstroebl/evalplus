

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
    # Use a state variable to keep track of the current state of the fib4 number sequence
    n_list = [0, 1, 2, 3, 4]
    state = 0
    
    # Use a while loop to iterate through each state in the sequence
    while state <= n:
        # If the current state is 0 or 1, simply return that state
        if state in [0, 1]:
            return state
        # Otherwise, calculate the next state using the recursive formula
        else:
            next_state = fib4(state)
            state += 1
        
    # If the current state is greater than n, return the final state
    return next_state
