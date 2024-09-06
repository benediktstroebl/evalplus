
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
    # create a list to store the numbers
    numbers = []
    # loop through the values of n
    for i in range(1, n + 1):
        # if n is even, add the recurrence to the numbers list
        if i % 2 == 0:
            numbers.append(i)
        # if n is odd, use the recurrence to calculate the next number and add it to the numbers list
        else:
            numbers.append(numbers[i // 2] + numbers[i // 2 + 1] + numbers[i // 2 - 1])
    # return the list of numbers
    return numbers
