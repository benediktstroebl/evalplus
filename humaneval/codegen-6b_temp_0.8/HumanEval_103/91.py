
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
    ans = str(int((n+m)/2))
    size = len(ans)
    if n<m:
        return -1
    elif n>m:
        return -1
    elif size<32:
        return "0b"+"".join("0" if c=="0" else "1" for c in ans)
    else:
        return -1