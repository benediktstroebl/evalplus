
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
    n0 = 3
    n1 = 3
    n2 = 1
    list_out = [n0, n1, n2]
    
    if n < 0:
        return []
    
    if n < 3:
        return list_out[:n + 1]
    
    n_in = 5
    
    while n_in <= n:
        list_out.append(list_out[n_in - 3] + list_out[n_in - 2] + list_out[n_in - 1])
        n_in += 1
    
    return list_out
