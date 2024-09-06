def rounded_avg(n, m):
    diff = m - n
    if diff > 0 or (diff == 0 and m > n):
        return -1
    total = (m + n) // 2
    avg = total
    rounded = avg
    return f"0b{int(rounded):b}"