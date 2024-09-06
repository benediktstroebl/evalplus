def rounded_avg(n, m):
    avg = (n + m) // 2
    if n > m:
        return -1
    rounded = avg % 1
    return "-1" if rounded < 0 else f"0b{int(rounded):b}"