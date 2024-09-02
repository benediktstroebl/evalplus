
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

    # Variables
    min_integer = min(n, m)
    max_integer = max(n, m)

    # Calculation
    rounded_sum = 0
    for i in range(min_integer, max_integer + 1):
        rounded_sum += i
    rounded_sum = rounded_sum / (max_integer - min_integer + 1)
    rounded_sum = int(round(rounded_sum))

    if rounded_sum < 0:
        return -1
    else:
        return bin(rounded_sum)

