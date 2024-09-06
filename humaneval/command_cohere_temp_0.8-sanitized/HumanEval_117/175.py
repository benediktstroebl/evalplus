def count_consonants(word):
    count = 0
    for char in word:
        if char.isalpha():
            if char in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
                count += 1
        elif char.isspace():
            continue
        else:
            pass
    return count
def select_words(s, n):
    words = s.split()
    result = [word for word in words if count_consonants(word) == n]
    return result