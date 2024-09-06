def count_upper(s):
    cnt = 0
    for i in range(len(s)):
        if s[i] in 'AEIOU' and s[i].isupper() and (i%2==0):
            cnt += 1
    return cnt