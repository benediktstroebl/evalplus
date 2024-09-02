
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
    result = 0
    for i in range(n, m+1):
        result = result + (i // 2)
    result = result // 2
    result = str(result).zfill(1)
    return result

input = int(input("Enter n: "))
input = int(input("Enter m: "))
result = rounded_avg(input, input)
