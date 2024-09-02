
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
    try:
        n, m = int(n), int(m)
        if n > m:
            return -1
        if n == m:
            return "0b{}".format(n)
        a, b = n, m
        while b - a > 1:
            mid = (a + b) // 2
            bin_mid = "0b{}".format(mid)
            if bin_mid >= "0b{}".format(m):
                a = mid
            else:
                b = mid
        return "0b{}".format(a)
    except:
        return -
