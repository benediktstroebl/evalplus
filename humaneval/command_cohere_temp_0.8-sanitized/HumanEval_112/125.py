def reverse_delete(s, c):
    delete = [char for char in c]
    pm = []
    for i in s:
        if i not in delete:
            pm.append(i)
    pm = pm[::-1]
    if pm == s:
        return ('', True)
    elif pm == s[::-1]:
        return (pm, False)
    else:
        return ('', False)