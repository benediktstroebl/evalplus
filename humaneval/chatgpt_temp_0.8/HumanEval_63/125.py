# CANNOT PARSE CODE SNIPPET
def fibfib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        a, b, c = 1, 1, 0
        for i in range(3, n+1):
            # Compute the FibFib number for index i using dynamic programming
            temp = a + b + c
            c = b
            b = a
            a = temp
        return a - b - c
