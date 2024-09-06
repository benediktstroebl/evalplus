def rounded_avg(n, m):
    total = (m + n) // 2
    count = 1
    # Iterate through integers between n and m inclusive, and count unique numbers.
    for i in range(n, m + 1):
        if i != n and i != m:
            count += 1
        total += 1
    if count == 0:
        return "-1"  # No unique numbers in the range
    rounded_total = total // count
    return f"0b{bin(rounded_total)[2:]}"