
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
    # use python's built-in function range() to generate a list of numbers from 0 to n
    # you can use start=1 to generate 0, 1, 2
    # instead of n+1, you can use n-1
    # also, you can use n-10 instead of n-1, if you are using python 3
    # you can use n//2 to get n mod 2, if you are using python 3
    numbers = range(n+1)
    # print the first 2 numbers for reference
    # if n is odd, use the recurrence relation
    # if n is even, use the first 2 numbers
    # if n is 0, print an empty list
    if n % 2 == 0:
        print(numbers[:2])
    elif n % 2 == 1:
        print(numbers[:3])
    else:
        print([])
    return numbers
