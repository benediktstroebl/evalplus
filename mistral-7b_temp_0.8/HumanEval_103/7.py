
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

    # Print a binary representation of n through m (including n and m) rounded to
    # the nearest integer
    # n is less than or equal to m
    # n and m are positive integers

    # if n is greater than m return -1
    if n > m:
        return -1

    # use list comprehension to make list from n to m (including n and m)
    # n = 1
    # m = 5
    # list = [1, 2, 3, 4, 5]
    list = [i for i in range(n, m+1)]

    # calculate the sum of the list
    sum_of_list = sum(list)

    # calculate the average
    avg = sum_of_list / len(list)

    # round the average
    rounded_avg = round(avg)

    # convert the rounded_avg to binary
    rounded_avg_binary = '{0:b}'.format(rounded_avg)

    # return rounded_avg_binary
    return rounded_avg_binary

