
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
    from fractions import Fraction
    n, m = n, m
    if m < n:
        n, m = m, n
    if n > m:
        return -1
    d = Fraction((m-n+1),2)
    num = d.numerator
    den = d.denominator
    #return str(bin(num//den))[2:]
    return bin(num//den).replace("0b", "")
    #return str(int(num/den))
    #return str(num//den)
    #return bin(num//den)[2:]
