
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
    n_to_round = max(n, m)
    total = n_to_round // m
    remainder = n_to_round % m
    avg = (total + remainder) // 2
    binary = bin(avg)
    if binary[0] == '0':
        binary = '0' + binary[1:]
    return binary
