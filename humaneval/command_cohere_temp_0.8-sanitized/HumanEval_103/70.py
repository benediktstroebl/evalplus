def rounded_avg(n, m):
    total = (m + n) // 2
    count = m - n + 1
    if count == 0:
        return "-1"
    rounded_total = round(total)
    if rounded_total == int(rounded_total):
        return f"0b{bin(rounded_total)[2:]}"
    else:
        return "-1"