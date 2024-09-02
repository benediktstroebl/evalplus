
def rounded_avg(n, m):
    """You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m). 
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.
    Example:
    rounded_avg(1, 5) => "0b11"
    rounded_avg(7, 5) => -1
    rounded_avg(10, 20) => "0b1111"
    rounded_avg(20, 33) => "0b11010"
    """
    # check n > m
    if n > m:
        return -1
    # sum numbers from n to m
    total = sum(range(n,m+1))
    # calculate the average of numbers from n to m
    average = total / (m - n + 1)
    # convert the average to binary
    binary_average = bin(average)
    # round the binary average to the nearest integer
    rounded_binary_average = round(average)
    # return the result
    return rounded_binary_average

