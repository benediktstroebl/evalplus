
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
    avg = ""
    if n == m:
        return "0b1"

    output = ""
    if n > m:
        avg = "-"
    elif n < m:
        n, m = m, n
    for i in range(m-n+1):
        output += "0"
    for i in range(n-1):
        output += "1"
    output = output[::-1]

    for i in range(int(len(output)/2)):
        avg += output[i]
    return avg[::-1]
