
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
    a, b, c = 0, 1, 1
    list_of_numbers = [a, b, c]
    while b < n:
        if b % 2 == 0:
            list_of_numbers.append(a)
            a = b + c
            b = b + c
        else:
            list_of_numbers.append(a)
            list_of_numbers.append(b)
            c = a + b + c
            b = c
    list_of_numbers.append(c)
    return list_of_numbers
