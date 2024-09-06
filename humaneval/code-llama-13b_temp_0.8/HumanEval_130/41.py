
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
    # My solution.
    # ...
    # I'm not sure if this is a good solution, but it works.
    if n == 1:
        return [3]
    elif n == 0:
        return []
    else:
        L = [3]
        for i in range(2, n + 1):
            if i % 2 == 0:
                L.append(1 + (i / 2))
            else:
                L.append(L[i - 1] + L[i - 2] + L[i + 1])
        return L
    
    # Other solutions
    # def tri(n):
    #     if n == 0:
    #         return []
    #     T = [1, 3]
    #     for i in range(2, n + 1):
    #         T.append(T[i - 2] + T[i - 1] + T[i])
    #     return T

    # def tri(n):
    #     if n == 0:
    #         return []
    #     T = [1, 3]
    #     for i in range(2, n + 1):
    #         T.append(T[i - 2] + T[i - 1] + T[i])
    #     return T

    # def tri(n):
    #     if n == 0:
    #         return []
    #     if n == 1:
    #         return [3]
    #     T = [1, 3]
    #     for i in range(2, n + 1):
    #         T.append(T[i - 2] + T[i - 1] + T[i])
    #     return T

    # def tri(n):
    #     if n == 0:
    #         return []
    #     if n == 1:
    #         return [3]
    #     T = [1, 3]
    #     for i in range(2, n + 1):
    #         T.append(T[i - 2]
