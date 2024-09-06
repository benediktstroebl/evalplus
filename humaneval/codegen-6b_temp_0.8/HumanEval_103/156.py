
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
    (end, start) = (max(n, m), min(n, m))
    rounded = int(2**int(str(start).replace('0b', '').replace('-', ''), 2))
    num = end/2 - start/2
    while rounded < end:
        rounded = float('{0:.2f}'.format(rounded))
        if rounded > end - start/2:
            return -1
        rounded = int(rounded)
        num += 1
    if start%2 == 1:
        return '-' + str(num) + 'b' + str(bin(num)[2:])
    else:
        return str(bin(num)[2:])