def rounded_avg(n, m):
    diff = m - n
    if diff > 0 or (diff == 0 and m == n):
        return "-1"
    avg = (n + m) // 2
    return f"0b{bin(round(avg))[2:]}"