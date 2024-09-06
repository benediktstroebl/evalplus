def count_consonants(word):
    cnt = 0
    for char in word:
        if char.isalpha():
            if char in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
                cnt += 1
    return cnt
def select_words(s, n):
    words = s.split()
    result = []
    for word in words:
        if count_consonants(word) == n:
            result.append(word)
    return result
input_string = "Mary had a little lamb"
n = 3
result = select_words(input_string, n)