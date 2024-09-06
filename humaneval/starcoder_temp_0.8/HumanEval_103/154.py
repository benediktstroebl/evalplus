
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
    # Your code here
    if n>m:
        return -1
    else:
        n=list(bin(n)[2:])
        m=list(bin(m)[2:])
        while len(n)<len(m):
            n.append("0")
        while len(m)<len(n):
            m.append("0")
        a=list()
        for i in range(len(n)):
            if int(n[i])+int(m[i])>1:
                a.append(1)
            else:
                a.append(0)
        return int("".join(str(i) for i in a),2)
