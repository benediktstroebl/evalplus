def reverse_delete(s, c):
    delete = [x for x in s if x not in c]
    delete.reverse()
    delete = delete + ['']
    if delete == delete[::-1]:
        return delete, True
    else:
        return delete, False