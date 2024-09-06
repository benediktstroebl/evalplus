
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
    remainder = m % 2
    sum = 0
    for i in range(n, m+1):
        if i % 2 == 0:
            sum += i
        else:
            sum += i - 1
    if remainder == 0:
        return sum // 2
    else:
        return (sum // 2) + (1 if sum % 2 == 1 else 0)

n, m = map(int, input().split())
result = rounded_avg(n, m)
print(result // 2)