
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

    def round_half_up(num):
        """Round a number up if the fractional part is .5 or greater. 
        Examples:
        0.5 -> 1
        1.5 -> 2
        -0.5 -> -1
        -1.5 -> -2
        """
        from math import floor, ceil

        if num >= 0:
            return int(ceil(num))
        else:
            return int(floor(num))

    if m < n:
        return -1
    elif n == m:
        return str(bin(n))[2:]
    else:
        a = sum(range(n, m + 1))
        b = round_half_up(a/len(range(n, m + 1)))
        return str(bin(b))[2:]
