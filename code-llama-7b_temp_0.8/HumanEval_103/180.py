
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
    if n > m:
        return -1
    total = 0
    # Compute the average
    for i in range(n, m+1):
        total += i
    average = total / (m - n + 1)
    # Compute the binary
    bit_string = "0b"
    while average != 0:
        if average >= 1:
            bit_string += "1"
            average -= 1
        else:
            bit_string += "0"
            average = average * 2
    return bit_string
