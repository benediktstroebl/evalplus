def reverse_delete(s, c):
    delete = [x for x in s if x not in c]
    delete.reverse()
    delete = delete + ['']
    delete_string = ''.join(delete)
    return delete_string, delete_string == delete_string[::-1]