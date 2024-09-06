
def tri(n):
    """Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
    the last couple centuries. However, what people don't know is Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    For example:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8 
    You are given a non-negative integer number n, you have to a return a list of the 
    first n + 1 numbers of the Tribonacci sequence.
    Examples:
    tri(3) = [1, 3, 2, 8]
    """
    def rec_tri(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 3
        elif n % 3 == 0:
            return rec_tri(n // 3) * rec_tri(n // 3) * rec_tri(n // 3)
        elif n % 3 == 1:
            return rec_tri((n - 1) // 3) * rec_tri((n - 2) // 3) * rec_tri((n - 1) // 3) + rec_tri((n - 1) // 3)
        else:
            return rec_tri((n - 2) // 3) * rec_tri((n - 2) // 3) * rec_tri((n - 2) // 3) + rec_tri((n - 2) // 3) * rec_tri((n - 1) // 3) * rec_tri((n - 2) // 3)

    list_tri = [0, 1, 2, 3]
    if n == 0:
        return list_tri[:2]
    for i in range(4, n + 2):
        list_tri.append(rec_tri(i))
    return list_tri[:n + 1]
