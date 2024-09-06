def rounded_avg(n, m):
    if n > m:
        return -1
    # Find the average
    total = (m + n) // 2
    # Round the average to the nearest integer
    avg = int(round(total))
    # Convert to binary
    return f"0b{bin(avg)[2:]}"