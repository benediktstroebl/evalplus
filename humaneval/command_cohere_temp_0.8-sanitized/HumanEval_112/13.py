def reverse_delete(s, c):
    delete = [char for char in c]
    reverse = s[::-1]
    pm = 0
    for i in range(len(s)):
        if s[i] in delete:
            pm += 1
        elif reverse[i] in delete:
            pm += 1
    if pm == len(s) // 2:
        return s, True
    else:
        return s, False