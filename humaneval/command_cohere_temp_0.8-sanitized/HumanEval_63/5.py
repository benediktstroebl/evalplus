def fibfib(n):
    # handle special cases
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    # otherwise, iterate through previous values and add them up
    return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)