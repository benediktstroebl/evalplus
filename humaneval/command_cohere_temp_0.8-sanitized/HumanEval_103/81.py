def rounded_avg(n, m):
    average = (n + m) // 2
    if n > m:
        return -1
    binary_string = bin(round(average))[2:]
    return binary_string if binary_string[0] == '0' else binary_string[1:]