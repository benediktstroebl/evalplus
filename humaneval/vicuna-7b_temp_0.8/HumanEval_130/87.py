
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
    # initialize variables to store the next numbers
    a = 3
    b = 1
    c = 1
    # loop through the numbers
    for i in range(n+1):
        # calculate the next number
        if n % 2 == 0:
            next_number = b
        else:
            next_number = a + b + c
        # append the next number to the list
        numbers.append(next_number)
        # update the variables
        b = a
        a = c
        c = next_number
    # return the list
    return numbers
