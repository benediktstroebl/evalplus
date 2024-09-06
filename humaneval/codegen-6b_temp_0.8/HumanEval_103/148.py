
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
    if n == 0:
        n = 1
    if m == 0:
        m = 1
    numerator = int(n)
    denominator = int(m)
    s = []
    while numerator <= denominator:
        s.append(format(numerator, 'b'))
        numerator += 1
    total = 0
    for x in s:
        for y in x:
            if y == '1':
                total += 1
    total = format(total, 'b')
    total = total[::-1]
    remainder = len(total) - len(s)
    answer = total[remainder:]
    answer = answer[::-1]
    return answer
