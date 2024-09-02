
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
    # define max_val as the larger number in n and m
    max_val = n if n > m else m

    # define min_val as the smaller number in n and m
    min_val = m if n > m else n

    # handle case when n > m
    if min_val > max_val:
        return -1

    # compute average
    avg = (min_val + max_val) / 2

    # convert average to binary
    binary = bin(int(avg))

    return binary

