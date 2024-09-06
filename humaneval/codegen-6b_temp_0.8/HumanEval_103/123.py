
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
    b = bin(n)
    a = b[2:]
    b = bin(m)
    c = b[2:]
    if a > c:
        return -1
    d = len(a)
    i = 0
    e = 0
    if d > 1:
        while i < d:
            s = a[:d - i - 1] + "0" + a[d - i - 1:]
            e += s.count("1")
            i += 1
    else:
        while i < d:
            s = a[:d - i - 1] + "0" + a[d - i - 1:]
            e += s.count("1")
            i += 1
    return bin(e // (d - i + 1))[2:]

