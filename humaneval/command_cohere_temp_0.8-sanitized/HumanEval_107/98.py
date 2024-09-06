def even_odd_palindrome(n):
    s = str(n)
    cnt = 0
    for i in range(len(s)//2):
        if s[i] == s[-(i+1)]:
            cnt += 1
    even, odd = 0, 0
    for i in range(1, n+1):
        if str(i) == str(i)[::-1]:
            if i%2 == 0:
                even += 1
            else:
                odd += 1
    return (even, odd)