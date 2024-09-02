
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
    bin_str = ""
    for i in range(n, m+1):
        bin_str += str(i)
    round_bin_str = round_to_n_bit_places(bin_str, 2)
    print(round_bin_str)
    return bin_to_int(round_bin_str)

