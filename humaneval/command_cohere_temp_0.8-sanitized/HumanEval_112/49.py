def reverse_delete(s, c):
    delete = [char for char in c]
    reverse = s[::-1]
    n = len(s)
    for i in range(n):
        if s[i] in delete or reverse[i] in delete:
            s = s[:i] + s[i+1:]
            break
    else:
        return s, True
s = "abcdef"
c = "b"