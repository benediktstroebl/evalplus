
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
    # add n and m
    num = n + m
    # get number of digits in num
    num_digits = len(str(num))
    # check if num is greater than 10000
    if num > 10000:
        return -1
    # calculate average
    avg = (n + m) // 2
    # convert avg to binary
    avg_bin = str(avg).zfill(num_digits)
    return avg_bin