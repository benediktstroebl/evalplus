def starts_one_ends(n):
    cnt = 0
    for i in range(n):
        num = '1' + '9' * (n - 1) + '1'
        cnt += int(num) + int(str(10 ** (n - 1)) + num)
    return cnt