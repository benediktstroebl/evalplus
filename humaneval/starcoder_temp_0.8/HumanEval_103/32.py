
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
    # # WAY 1
    # if n > m:
    #     return -1
    # else:
    #     lst = []
    #     for i in range(n, m+1):
    #         lst.append(i)
    #     average = sum(lst) / len(lst)
    #     rounded = round(average)
    #     bin_form = bin(rounded)
    #     return bin_form
    # # WAY 2
    # if n > m:
    #     return -1
    # else:
    #     sum_of_nums = 0
    #     while n <= m:
    #         sum_of_nums += n
    #         n += 1
    #     average = sum_of_nums / (m - n + 1)
    #     rounded = round(average)
    #     bin_form = bin(rounded)
    #     return bin_form
