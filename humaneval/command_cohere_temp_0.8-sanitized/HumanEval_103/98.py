def rounded_avg(n, m):
    binary_string = '-1'
    if n > m:
        return binary_string
    total = (n + m) // 2
    count = 1
    temp_avg = 0
    while count <= m - n + 1:
        temp_avg += total
        count += 1
        total = total - n + m
    temp_avg = int(temp_avg)
    return binary_string if temp_avg % 1 else bin(temp_avg)[2:]