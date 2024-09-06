def reverse_delete(s, c):
    delete = [char for char in c]
    reverse = s[::-1]
    ne_delete = [char for char in delete if char not in reverse]
    result = ''.join(ne_delete)
    if result == result[::-1]:
        return result, True
    else:
        return result, False