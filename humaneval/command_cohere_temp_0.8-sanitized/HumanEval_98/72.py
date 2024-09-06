def count_upper(s):
    cnt = 0
    for i in range(len(s)):
        if i % 2 == 0 and s[i].isupper() and s[i] in 'AEIOU':
            cnt += 1
    return cnt