def reverse_delete(s, c):
    delete = [char for char in c]
    reverse = s[::-1]
    pm = 0
    for i in range(len(s)):
        if s[i] in delete and reverse[pm] != s[i]:
            pm += 1
    temp = s[pm::]
    if temp == temp[::-1]:
        return (temp, True)
    else:
        return (temp, False)