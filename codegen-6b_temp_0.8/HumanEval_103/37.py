
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
    part1 = ""
    part2 = ""
    if n > m:
        return -1
    else:
        avg = 0
        for i in range(n, m+1):
            part1 += bin(i)[2:]
        for char in part1:
            avg += int(char)
        part2 = bin(avg)[2:]
        if len(part2) % 2 == 1:
            part2 = '0' + part2
        return part2
