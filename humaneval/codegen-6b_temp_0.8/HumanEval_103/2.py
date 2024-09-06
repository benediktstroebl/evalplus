
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
    assert n >= 0 and m > n
    if m == n:
        return "0b" + bin(n)[2:]
    lhs = bin(n)[2:]
    rhs = bin(m)[2:]
    len_lhs = len(lhs)
    len_rhs = len(rhs)
    # get rid of zeros
    if len_lhs < len_rhs:
        lhs = "0"*(len_rhs-len_lhs) + lhs
    else:
        rhs = "0"*(len_lhs-len_rhs) + rhs
    # find the common prefix
    while len_lhs > 0 and len_rhs > 0:
        if lhs[-1] != rhs[-1]:
            break
        lhs = lhs[:-1]
        rhs = rhs[:-1]
    # the longest common prefix is the common prefix
    result = bin(int(lhs, 2) + int(rhs, 2))[2:]
    result = "0"*(len_lhs + len_rhs - len(result)) + result
    return result

