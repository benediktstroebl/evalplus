def even_odd_palindrome(n):
    s = str(n)
    cnt = 0
    for i in range(len(s)-1):
        if s[i] == s[len(s)-1-i]:
            cnt += 1
    even, odd = 0, 0
    for i in range(1, n+1):
        if str(i) == str(i)[::-1] and i % 2 == 0:
            even += 1
        elif str(i) == str(i)[::-1] and i % 2 != 0:
            odd += 1
    return (even, odd)