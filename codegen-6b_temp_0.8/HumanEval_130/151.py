
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
    answer = [3]
    n_1, n_2, n_3 = (4, 3, 2)
    while len(answer) < (n + 1):
        if len(answer) == 1:
            answer = [1, 3, 2, 7]
        elif len(answer) == 2:
            answer = [1, 3, 2, 7, 14]
        else:
            answer.append(n_3)
            n_3 = n_2 + n_1 + n_3
            n_2 = n_1 + n_3
            n_1 = n_3

    return answer
