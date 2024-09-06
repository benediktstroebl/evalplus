def fizz_buzz(n):
    cnt = 0
    for i in range(1, n+1):
        if i%11==0 or i%13==0:
            num = str(i)
            cnt += num.count('7')
    return cnt