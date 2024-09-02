
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
    # If n is even, we have to take the first two numbers of the sequence
    # and add the next number to get the n+1 number
    if n % 2 == 0:
        tri_list = [3, 1, n // 2]
        n_list = list(range(1, n))
        tri_list.extend(n_list)
        return tri_list
    # If n is odd, we have to use the recurrence relation to calculate the n+1 number
    else:
        tri_list = [1, n // 2, 1]
        n_list = list(range(1, n + 1))
        tri_list.extend(n_list)
        return tri_list
