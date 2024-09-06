def starts_one_ends(n):
    cnt = 0
    for i in range(10, n + 1):
        num = str(i)
        if num[0] == '1' or num[-1] == '1':
            cnt += 1
    return cnt