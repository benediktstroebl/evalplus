
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
    def bin_to_int(binary):
        return int(binary, 2)

    def int_to_bin(number):
        return bin(number)[2:]

    def merged(_n, _m, _bin):
        b_1 = _bin[:_n]
        b_2 = _bin[_n:]
        return b_1 + _bin[:_m] + b_2

    m += 1
    n += 1

    if n > m:
        return -1

    if m == n:
        return int_to_bin(n)

    return int_to_bin(int((m + n) / 2))

