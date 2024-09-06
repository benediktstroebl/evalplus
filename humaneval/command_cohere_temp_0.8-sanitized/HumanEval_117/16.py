def count_consonants(word):
    return sum(1 for char in word if char in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
def select_words(s, n):
    words = [word for word in s.split() if word]
    return [word for word in words if count_consonants(word) == n]