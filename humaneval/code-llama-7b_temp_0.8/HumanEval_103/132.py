
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
    # find the average of the two numbers
    # round it
    # convert the rounded number to binary
    # return the binary number
    if n > m:
        return -1
    else:
        average = (n+m)/2
        rounded_average = round(average)
        return bin(rounded_average)[2:]
    pass
