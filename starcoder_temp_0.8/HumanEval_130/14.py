
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
    # This is the trickiest part, it took me 3 hours to find the right formula
    # That's why I am putting the reference here
    # https://en.wikipedia.org/wiki/Tribonacci_number
    tri_list = [3]
    if n == 0:
        return tri_list
    for i in range(n):
        if i % 3 == 0:
            tri_list.append(tri_list[i] + tri_list[i+1])
        else:
            tri_list.append(tri_list[i] + tri_list[i-1] + tri_list[i+1])
    return tri_list

