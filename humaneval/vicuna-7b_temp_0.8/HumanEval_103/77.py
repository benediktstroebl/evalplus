
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
    result = 0
    for i in range(n, min(m+1, len(str(n)))+1):
        result += int(n)
    result = round(result / 2)
    return str(result).zfill(len(str(n))-1).rjust(len(str(m)), '0')

inputs = [
    (1, 5),
    (7, 5),
    (10, 20),
    (20, 33),
    (21, 25),
    (-1, 10)
]

for i in inputs:
    print(rounded_avg(*i))