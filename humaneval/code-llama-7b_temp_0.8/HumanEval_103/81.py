
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
    # calculate the avg and round it
    avg = (m + n) / 2.0
    avg_rounded = round(avg)
    # convert avg to binary
    avg_b = bin(avg_rounded)
    print(avg_b)
    # return -1 if n > m
    if n > m:
        return -1
    # return the rounded avg in binary
    return avg_b
