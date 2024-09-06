def rounded_avg(n, m):
    if n > m:
        return -1
    sum_ = 0
    count = 0
    for i in range(n, m + 1):
        sum_ += i
        count += 1
    avg = int(sum_/count)
    if avg % 2 == 0:
        return f"0b{bin(avg)[2:]}"
    else:
        return f"0b{bin(avg + 1)[2:]}"