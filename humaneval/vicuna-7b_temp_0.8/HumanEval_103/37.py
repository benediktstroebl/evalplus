
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
    # The formula for the average is (n + (m - n + 1)) / 2
    avg = (n + (m - n + 1)) // 2
    # convert avg to binary and round to the nearest integer
    binary_avg = round(avg)
    # return binary_avg
    return binary_avg
