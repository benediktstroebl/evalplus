def rounded_avg(n, m):
    if n > m:
        return -1
    num_sum = (n + m) // 2
    rounded_sum = round(num_sum)
    return f"0b{bin(rounded_sum)[2:]}"