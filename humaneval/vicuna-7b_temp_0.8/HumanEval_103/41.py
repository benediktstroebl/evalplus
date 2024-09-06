
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
    # you can compute the range by subtracting m from n
    range_start = n - 1
    range_end = m
    
    # you can compute the sum of the numbers in the range
    sum = 0
    for i in range(range_start, range_end+1):
        sum += i
    
    # you can compute the average by dividing the sum by the number of integers in the range
    average = sum / (range_end - range_start + 1)
    
    # round the average to the nearest integer
    average_bin = int(round(average))
    
    return average_bin
