def count_consonants(word):
    return sum(1 for char in word if char in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
def select_words(s, n):
    words = s.split()
    result = [word for word in words if count_consonants(word) == n]
    return result