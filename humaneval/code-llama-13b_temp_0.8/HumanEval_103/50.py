
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
    # get the total value
    value = sum(range(n, m+1))
    avg = (n+m) // 2
    # round the average up if there is a remainder
    if value % (m-n+1) != 0:
        avg += 1
    # return -1 if n is greater than m
    if n > m:
        return -1
    else:
        return avg

