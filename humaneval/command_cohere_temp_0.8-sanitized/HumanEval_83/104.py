def starts_one_ends(n):
    cnt = 0
    for i in range(n):
        num = 1
        for j in range(n-i-1):
            num = num * 10 + 1
            cnt += 1
        num = 10 * (num // 10) + 1
        cnt += 1
    return cnt