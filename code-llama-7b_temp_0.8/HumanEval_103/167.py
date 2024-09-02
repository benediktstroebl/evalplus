
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
    # check if m > n
    if m < n:
        return -1
    # create empty array to store values
    values = []
    # while loop to add values from n to m inclusive
    while n <= m:
        values.append(n)
        n = n + 1
    # sum all values
    total = sum(values)
    # return average to 2 decimal places
    return int(round(total / len(values), 2))
