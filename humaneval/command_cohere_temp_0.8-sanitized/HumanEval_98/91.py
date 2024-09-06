def count_upper(s):
    cnt = 0
    for i in range(len(s)):
        if s[i].isupper() and s[i] in 'AEIOU' and (i%2==0):
            cnt += 1
    return cnt