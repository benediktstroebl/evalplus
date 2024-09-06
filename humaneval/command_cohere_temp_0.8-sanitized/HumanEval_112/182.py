def reverse_delete(s, c):
    delete = [char for char in c]
    reverse = s[::-1]
    result = ''.join(char for char in s if char not in delete and char in reverse)
    return result, result == result[::-1]