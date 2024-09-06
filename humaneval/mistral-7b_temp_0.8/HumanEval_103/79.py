
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
    result = []
    if n <= m:
        for i in range(n, m + 1):
            result.append(i)
        result_sum = sum(result)
        result_len = len(result)
        result_avg = result_sum/result_len
        bin_str = format(result_avg, 'b')
        return bin_str
    else:
        return -1
